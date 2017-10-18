#environment: arc pro 1.4-assume data (linked below) are already in the default gdb in the project
#script is only relevant for data as linked
#Estimate number of Business and Employees within each PDA
#Use a Point in poly method that calculates the totals for each PDA.
import arcpy
arcpy.management.AddSpatialIndex("L0gis_ABAG_Priority_Developm1", 0, 0, 0) #data source: http://mtc.maps.arcgis.com/home/item.html?id=ec0440c9691242e9880708f91eb215bf
arcpy.management.AddSpatialIndex("ca_businesses", 0, 0, 0) #data source: https://mtcdrive.box.com/s/oyj6twno0gjtp3y6w2nswq5xak4qltju
arcpy.analysis.SpatialJoin("L0gis_ABAG_Priority_Developm1",
							 "ca_businesses",
							 r"C:\Users\tbuckl\Documents\ArcGIS\Projects\pdas_businesses\pdas_businesses.gdb\pda_businesses3",
							 "JOIN_ONE_TO_ONE",
							 "KEEP_ALL",
							 'joinkey "joinkey" true true false 20 Text 0 0,First,#,L0gis_ABAG_Priority_Developm1,joinkey,0,20;sum_emplymnt "EMPNUM" true true false 8 Double 0 0,Sum,#,ca_businesses,EMPNUM,-1,-1;pda_name "NewField" true true false 0 Text 0 0,First,#,L0gis_ABAG_Priority_Developm1,name,0,0',
							 "INTERSECT", None, None)


arcpy.management.DeleteField("pda_businesses3",
							 "pda_name;TARGET_FID")

arcpy.management.AddJoin("pda_businesses3",
						 "joinkey",
						 "L0gis_ABAG_Priority_Developm1",
						 "joinkey",
						 "KEEP_ALL")

arcpy.management.AlterField("pda_businesses_out2",
							 "Join_Count",
							 "business_count",
							 "business_count",
							 "LONG",
							 4, "NULLABLE",
							 False)

arcpy.conversion.FeatureClassToFeatureClass("pda_businesses3",
 
	r"C:\Users\tbuckl\Documents\ArcGIS\Projects\pdas_businesses\pdas_businesses.gdb",
 "pda_businesses_out2",
 None, 'Join_Count "Join_Count" true true false 4 Long 0 0,First,#,pda_businesses3,pda_businesses3.Join_Count,-1,-1;joinkey "joinkey" true true false 20 Text 0 0,First,#,pda_businesses3,pda_businesses3.joinkey,0,20;sum_emplymnt "EMPNUM" true true false 8 Double 0 0,First,#,pda_businesses3,pda_businesses3.sum_emplymnt,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,pda_businesses3,pda_businesses3.Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,pda_businesses3,pda_businesses3.Shape_Area,-1,-1;L0gis_ABAG_Priority_Developm1_name "name" true true false 254 Text 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.name,0,254;L0gis_ABAG_Priority_Developm1_lead "lead" true true false 254 Text 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.lead,0,254;L0gis_ABAG_Priority_Developm1_subregion "subregion" true true false 254 Text 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.subregion,0,254;L0gis_ABAG_Priority_Developm1_planstatus "planstatus" true true false 20 Text 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.planstatus,0,20;L0gis_ABAG_Priority_Developm1_abagstatus "abagstatus" true true false 20 Text 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.abagstatus,0,20;L0gis_ABAG_Priority_Developm1_futurept1 "futurept1" true true false 25 Text 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.futurept1,0,25;L0gis_ABAG_Priority_Developm1_grossacres "grossacres" true true false 8 Double 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.grossacres,-1,-1;L0gis_ABAG_Priority_Developm1_netacres "netacres" true true false 8 Double 0 0,First,#,pda_businesses3,L0gis_ABAG_Priority_Developm1.netacres,-1,-1', 
 None)

#needed to rename a field b/c the alias was from a legacy name but not the one assigned (groan...)
arcpy.management.AlterField("pda_2015_businesses_employment_2016",
							 "sum_emplymnt",
							 "sum_emplymnt",
							 "sum_emplymnt",
							 "DOUBLE",
							 8, "NULLABLE",
							 False)