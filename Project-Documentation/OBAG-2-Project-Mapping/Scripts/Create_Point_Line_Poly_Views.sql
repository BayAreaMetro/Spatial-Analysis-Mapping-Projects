CREATE VIEW RPD_OBAG_2_Project_Points
AS 
SELECT
	[_id] as OBJECTID,
	[ID] AS App_Proj_ID,
	[Proj_number] AS List_Proj_ID, 
	[Project],
	[MAP_Label],
	[MAP_Mode],
	[County],
	[Description_of_work],
	[MAP_project_name],
	[PDA_status],
	[Shape]
FROM [rpd].[MapApplicatonData] AS APP_DATA
LEFT JOIN [rpd].[RPD_OBAG_2_PROJECT_LIST] AS LIST 
ON APP_DATA.ID = LIST.Proj_number
WHERE (WKT LIKE 'POINT%' OR WKT LIKE 'MULTIPOINT%') AND Project = 'OBAG' 

CREATE VIEW RPD_OBAG_2_Project_Lines
AS 
SELECT
	[_id] as OBJECTID,
	[ID] AS App_Proj_ID,
	[Proj_number] AS List_Proj_ID, 
	[Project],
	[MAP_Label],
	[MAP_Mode],
	[County],
	[Description_of_work],
	[MAP_project_name],
	[PDA_status],
	[Shape]
FROM [rpd].[MapApplicatonData] AS APP_DATA
LEFT JOIN [rpd].[RPD_OBAG_2_PROJECT_LIST] AS LIST 
ON APP_DATA.ID = LIST.Proj_number
WHERE (WKT LIKE 'LINE%' OR WKT LIKE 'MULTILINE%') AND Project = 'OBAG'

CREATE VIEW RPD_OBAG_2_Project_Polygons
AS 
SELECT
	[_id] as OBJECTID,
	[ID] AS App_Proj_ID,
	[Proj_number] AS List_Proj_ID, 
	[Project],
	[MAP_Label],
	[MAP_Mode],
	[County],
	[Description_of_work],
	[MAP_project_name],
	[PDA_status],
	[Shape]
FROM [rpd].[MapApplicatonData] AS APP_DATA
LEFT JOIN [rpd].[RPD_OBAG_2_PROJECT_LIST] AS LIST 
ON APP_DATA.ID = LIST.Proj_number
WHERE (WKT LIKE 'POLYGON%') AND Project = 'OBAG'

