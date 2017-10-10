"""
   adapted from the examples section of the ArcREST package

   requires a credentials.json file with login details for the agol site you want to publish to. 

   also requires a pdf.jpg file for a boilerplate thumbnail (600x400) in the script dir. 

"""
import arcrest
import json
import requests
import os
from arcresthelper import securityhandlerhelper

MOTM_URL = "https://raw.githubusercontent.com/BayAreaMetro/motm/master/motm.json"

SECURITY_INFO = {'security_type' : 'Portal',
                'username' : '',
                'password' : '',
                'org_url' : '',
                'proxy_url' : None,
                'proxy_port' : None,
                'referer_url' : None,
                'token_url' : None,
                'certificatefile' : None,
                'keyfile' : None,
                'client_id' : None,
                'secret_id' : None}

def trace():
    """
        trace finds the line, the filename
        and error message and returns it
        to the user
    """
    import traceback, inspect, sys
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    filename = inspect.getfile(inspect.currentframe())
    # script name + line number
    line = tbinfo.split(", ")[1]
    # Get Python syntax error
    #
    synerror = traceback.format_exc().splitlines()[-1]
    return line, filename, synerror


def get_filename_from_url(url_path):
    try:
        from urllib.parse import urlparse
    except ImportError:
        from urlparse import urlparse
    from os.path import basename
    disassembled = urlparse(url_path)
    filename= basename(disassembled.path)
    return(filename)

def get_file_at_url(url):
    if url != None:
        try:
            tmp_filename = get_filename_from_url(url)
            response = requests.get(url)
            with open(tmp_filename, 'wb') as f:
                f.write(response.content)
            return(tmp_filename)
        except:
            print("could not fetch pdf for item:{}".format(url))
    else:
        return("")

def add_item(securityinfo,filename,metadata):    
    try:
        shh = securityhandlerhelper.securityhandlerhelper(securityinfo)
        if shh.valid == False:
            print(shh.message)
        else:
            admin = arcrest.manageorg.Administration(
                securityHandler=shh.securityhandler)
            content = admin.content
            userInfo = content.users.user()
            itemParams = arcrest.manageorg.ItemParameter()
            itemParams.title = metadata['title']
            itemParams.description = metadata['description']
            itemParams.tags = metadata['tags']
            itemParams.type = metadata['type']
            itemParams.thumbnail = metadata['thumbnail']
            item = userInfo.addItem(
                itemParameters=itemParams,
                filePath= filename,
                overwrite=True,
                relationshipType=None,
                originItemId=None,
                destinationItemId=None,
                serviceProxyParams=None,
                metadata=None)
            print(item.title + " created")
            i = content.getItem(item.id)
            i.shareItem(everyone=True)
            return(item)

    except:
        line, filename, synerror = trace()
        print("error on line: %s" % line)
        print("error in file name: %s" % filename)
        print("with error message: %s" % synerror)

def add_motm_pdf(motm, securityinfo):
    if motm['link'][-3:] == "pdf": 
        motm['tags'] = 'motm'
        pdf_url = motm['link'] 
        pdf_name = get_file_at_url(pdf_url)

        #setup metadata to match agol
        motm['thumbnail'] = "pdf.jpg"
        keys_to_drop = ["year","author","image"]
        motm = drop_keys(motm,keys_to_drop)
    else:
        print("not a PDF")

    if pdf_name != "":
        motm['type'] = "PDF"
        item_metadata = add_item(securityinfo,pdf_name,motm)
    else:
        print("not a pdf")

def main():
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
        securityinfo = SECURITY_INFO
        securityinfo.update(credentials)
    
    motm_list = requests.get(MOTM_URL).json()

    for motm in motm_list:
        add_motm_pdf(motm, securityinfo)

def drop_keys(adict,keys_to_drop):
    for k in keys_to_drop:
        adict.pop(k,None) 
    return(adict)

if __name__ == "__main__":
    main()
