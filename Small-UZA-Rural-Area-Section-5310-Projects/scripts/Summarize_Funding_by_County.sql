--============================================================================================================
-- Summarize project by county, generating view with Project County, Project Total, and County Centroid
--============================================================================================================

CREATE VIEW PROJECT_5310_BY_COUNTY_2015_2017
AS 
SELECT newID() as OBJECTID, PROJ.PROJ_COUNTY, PROJ_TOTAL, Shape.STCentroid() as Shape
FROM [dbo].[MN_A8_UTM_Z10] AS COUNTIES 
RIGHT JOIN 
	(
	SELECT ABBREV_LOOKUP.County as PROJ_COUNTY, SUM(CAL_PROJ.Proposed_Total_Project) AS PROJ_TOTAL 
	FROM [dbo].[CALTRAINS_CTC_DRAFT_LIST_SMALL_UR_PROJECTS_DELETE] AS CAL_PROJ
	left JOIN [dbo].[CALTRAINS_COUNTY_ABBREV_LOOKUP] AS ABBREV_LOOKUP
	ON CAL_PROJ.Co = ABBREV_LOOKUP.County_Abbrev
	GROUP BY ABBREV_LOOKUP.County
	) PROJ
ON PROJ.PROJ_COUNTY = COUNTIES.NAME


