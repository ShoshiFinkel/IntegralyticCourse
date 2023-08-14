-- IF/ELSE

DECLARE @num_instructors INT

SELECT @num_instructors = COUNT(PersonID)
FROM CourseInstructor

IF @num_instructors > 10

BEGIN
PRINT 'There are more then 10 instructors.'
END

IF @num_instructors = 10
BEGIN
PRINT 'There are 10 instructors.'
END

ELSE
BEGIN
PRINT 'There are less then 10 instructors.'
END

-- TRY/CATCH
BEGIN TRY
	CREATE TABLE Person (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255))
END TRY

BEGIN CATCH
	SELECT 'An error occurred.'+
	ERROR_MESSAGE() AS ErrorMessage

	SELECT ERROR_LINE() AS ErrorLine,
		   ERROR_NUMBER() AS ErrorNumber,
		   ERROR_SEVERITY() AS ErrorSeverity,
		   ERROR_STATE() AS ErrorState
END CATCH
GO

CREATE TABLE #ErrorTable(ErrorMessage NVARCHAR(MAX),
	ErrorLine NVARCHAR(250),
	ErrorNumber NVARCHAR(250),
	ErrorSeverity NVARCHAR(250),
	ErrorState NVARCHAR(250))

BEGIN TRY
	CREATE TABLE Person (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255))
END TRY

BEGIN CATCH
	-- SELECT 'An error occurred.'+
	-- ERROR_MESSAGE() AS ErrorMessage

INSERT INTO #ErrorTable (ErrorMessage, ErrorLine, ErrorNumber, ErrorSeverity, ErrorState)
	SELECT ERROR_MESSAGE() AS ErrorMessage,
		   ERROR_LINE() AS ErrorLine,
		   ERROR_NUMBER() AS ErrorNumber,
		   ERROR_SEVERITY() AS ErrorSeverity,
		   ERROR_STATE() AS ErrorState
END CATCH





DECLARE @tableHTML NVARCHAR(MAX);
SET @tableHTML = 
	N'<h1>Error Handling</h1>'+
	N'<table border="1">'+
	N'<tr><thead><th>ErrorMessage</th><th>ErrorLine</th><th>ErrorNumber</th><th>ErrorSeverity</th><th>ErrorState</th></thead><tbody>'+
	CAST((SELECT 
	td = ErrorMessage,
	'',
	td = ErrorLine,
	'',
	td = ErrorNumber,
	'',
	td = ErrorSeverity,
	'',
	td = ErrorState,
	''
	FROM #ErrorTable
	FOR xml PATH ('tr'), TYPE)
	AS nvarchar(max))+
	N'<tbody></table>';

EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = @tableHTML,
	@subject = 'Error Handling',
	@body_format = 'HTML';

