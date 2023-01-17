--=====================================================================
-- Create view from spatial join of businesses & employment center 
-- polygons summarized by: 
	-- employment center (1 = Yes, 0 = No)
	-- MTC_CLASS 
	-- county 
-- Left join MTC_2012_NAICS_SECTOR_GROUPS as lookup table for MTC_CLASS by
-- NAICS two-digit sector code
--=====================================================================

CREATE VIEW NC_Mega_Region_Emp_Cent_Tot_Employment_By_Sector
AS
SELECT 
	 EMP_CENTERS.Emp_Center AS EMP_CENTER,
	 --SUBSTRING(BUSINESSES.NAICS, 1, 2) AS SECTOR,
	 MTC_CLASS.[MTC_CLASS_TITLE],    
	 SUM(BUSINESSES.EMPNUM) AS EMP_TOTAL,
	 BUSINESSES.COUNTY
FROM [dbo].[NC_MEGA_REGION_EMP_DENSITY_FC] AS EMP_CENTERS 
INNER JOIN [dbo].[NC_MEGA_REGION_BUSINESSES] AS BUSINESSES 
ON EMP_CENTERS.Shape.STIntersects(BUSINESSES.Shape) = 1
LEFT JOIN [dbo].[MTC_2012_NAICS_SECTOR_GROUPS] AS MTC_CLASS
ON SUBSTRING(BUSINESSES.NAICS, 1, 2) = MTC_CLASS.[NAICS_SECTOR]
GROUP BY 
	EMP_CENTERS.Emp_Center,
	--SUBSTRING(BUSINESSES.NAICS, 1, 2),
	MTC_CLASS.MTC_CLASS_TITLE,
	BUSINESSES.COUNTY


--=====================================================================
-- Create view which summarizes employment by sector for the 
-- Northern California Mega Region 
--=====================================================================

CREATE VIEW NC_Mega_Region_Total_Employment_By_Sector
AS 
SELECT
	MTC_CLASS.[MTC_CLASS_TITLE],
	SUM(BUSINESSES.EMPNUM) AS EMP_TOTAL
FROM [dbo].[NC_MEGA_REGION_BUSINESSES] AS BUSINESSES 
LEFT JOIN [dbo].[MTC_2012_NAICS_SECTOR_GROUPS] AS MTC_CLASS
ON SUBSTRING(BUSINESSES.NAICS, 1, 2) = MTC_CLASS.[NAICS_SECTOR]
GROUP BY 
	MTC_CLASS.MTC_CLASS_TITLE,
	MTC_CLASS.MTC_CLASS

--=====================================================================
-- Find Mega Region Total Jobs 
--=====================================================================

SELECT SUM(EMP_TOTAL)
FROM [dbo].[NC_Mega_Region_Total_Employment_By_Sector]