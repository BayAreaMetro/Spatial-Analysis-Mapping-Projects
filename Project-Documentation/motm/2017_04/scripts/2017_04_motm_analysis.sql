--==================================================================================================
/*
Calculate average median per sf home price in Bay Area
*/
--==================================================================================================

SELECT AVG([median_s_1])
FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
WHERE [cbsa_title] = 'San Francisco-Oakland-Hayward, CA'

--RESULT: 500.84511411

--==================================================================================================
/*
Calculate average school district performance in Bay Area, which is a measure of whether students
are at grade level, below grade level, or above grade level
*/
--==================================================================================================

SELECT AVG([gsmean_poo])
FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
WHERE [cbsa_title] = 'San Francisco-Oakland-Hayward, CA'

--RESULT: 0.27689426

--==================================================================================================
/*
Select districts with a mean commute less than 30 minutes
*/
--==================================================================================================

SELECT [district_n],[leaname],[NAME_LEA15]
FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
WHERE [cbsa_title] = 'San Francisco-Oakland-Hayward, CA'
AND [mean_commu] > 30

--RESULT: 36 districts with mean commute less than 30 minutes 

--==================================================================================================
/*
Add two additional columns to rank worst and best 
	-Worst ratings are for above average housing costs and below average school performance 
	-Best ratings are for below average housing costs and above average school performance 
*/
--==================================================================================================

ALTER TABLE [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
ADD 
	Worst_Rank numeric(38,8), 
	Best_Rank numeric(38,8)

--==================================================================================================
/*
**Best Rank**
Update school districts table with ranking based the following characteristics:
- Median per sf home price below Bay Area Average
- School district performance above Bay Area Average
*/
--==================================================================================================

UPDATE T1 
	SET [Best_Rank] = T2.Rank
FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED] AS T1
JOIN
(
	SELECT [district_n] AS District_Number,RANK() OVER (ORDER BY [median_s_1] ASC, [gsmean_poo] DESC ) as Rank
	
	FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
	WHERE
	(
	[cbsa_title] = 'San Francisco-Oakland-Hayward, CA'
	AND
	[median_s_1] < 500.84511411
	AND 
	[gsmean_poo] > 0.27689426
	)
) T2
ON T1.[district_n] = T2.District_Number

--SELECT * 
--FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
--WHERE best_rank is not null
--order by best_rank asc

--==================================================================================================
/*
**Worst Rank**
Update school districts table with ranking based the following characteristics:
- Median per sf home price above Bay Area Average
- School district performance below Bay Area Average
*/
--==================================================================================================

UPDATE T1 
	SET [Worst_Rank] = T2.Rank
FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED] AS T1
JOIN
(
	SELECT [district_n] AS District_Number,RANK() OVER (ORDER BY [median_s_1] DESC, [gsmean_poo] ASC ) as Rank
	
	FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
	WHERE
	(
	[cbsa_title] = 'San Francisco-Oakland-Hayward, CA'
	AND
	[median_s_1] > 500.84511411
	AND 
	[gsmean_poo] < 0.27689426
	)
) T2
ON T1.[district_n] = T2.District_Number

SELECT * 
FROM [dbo].[MOTM_NYT_JOIN_2013_UNIFIED]
WHERE worst_rank is not null
order by worst_rank asc