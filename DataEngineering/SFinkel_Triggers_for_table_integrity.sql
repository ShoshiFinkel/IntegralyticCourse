CREATE TRIGGER email_lower_grade_than_min ON [StudentGrade]
AFTER INSERT, UPDATE
AS
BEGIN
DECLARE @new_grade NVARCHAR(10), 
		@student_id NVARCHAR(10),
		@min_grade NVARCHAR(MAX),
		@message NVARCHAR(200),
		@subject NVARCHAR(100),
		@minimum_grade NVARCHAR(10),
		@enrollment_id NVARCHAR(10)

SELECT @new_grade= INSERTED.[Grade] FROM INSERTED
SELECT @student_id= INSERTED.[StudentID] FROM INSERTED
SELECT @enrollment_id = inserted.[EnrollmentID] FROM inserted
SET @min_grade = 'SELECT @grade = MIN(Grade)
			FROM StudentGrade
			WHERE StudentID = '+@student_id+
			'AND EnrollmentID != '+@enrollment_id+';'
EXEC sp_executesql @min_grade, N'@grade NVARCHAR(MAX) OUTPUT', @grade = @minimum_grade OUTPUT;

IF @new_grade < @minimum_grade 
BEGIN
SET @subject = 'New grade lower than min'
SET @message = 'Student ' + @student_id + ' got a lower grade than min grade. The new grade is ' + @new_grade +'.'
EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = @message,
	@subject = @subject,
	@body_format = 'HTML';
END
END
GO


-- Assigment 2
CREATE TRIGGER email_lower_grade_than_min_table ON [StudentGrade]
AFTER INSERT, UPDATE
AS
BEGIN
DECLARE @new_grade NVARCHAR(10), 
		@student_id NVARCHAR(10),
		@min_grade NVARCHAR(MAX),
		@message NVARCHAR(200),
		@subject NVARCHAR(100),
		@tableHTML  NVARCHAR(MAX),
		@minimum_grade NVARCHAR(10),
		@enrollment_id NVARCHAR(10)

SELECT @new_grade= INSERTED.[Grade] FROM INSERTED
SELECT @student_id= INSERTED.[StudentID] FROM INSERTED
SELECT @enrollment_id = inserted.[EnrollmentID] FROM inserted
SET @min_grade = 'SELECT @grade = MIN(Grade)
			FROM StudentGrade
			WHERE StudentID = '+@student_id+
			'AND EnrollmentID != '+@enrollment_id+';'
EXEC sp_executesql @min_grade, N'@grade NVARCHAR(MAX) OUTPUT', @grade = @minimum_grade OUTPUT;

IF @new_grade < @minimum_grade 

BEGIN
SET @subject = 'New grade lower than min - info';

SET @tableHTML = 
	N'<h1>Student ' + @student_id + ' got a lower grade than min grade.</h1>'+
	N'<table border="1">'+
	N'<tr><thead><th>CourseID</th><th>StudentID</th><th>Grade</th><th>FirstName</th><th>LastNmae</th></thead><tbody>'+
	CAST((SELECT 
	td = INSERTED.[CourseID],
	'',
	td = INSERTED.[StudentID],
	'',
	td = INSERTED.[Grade],
	'',
	td = p.FirstName,
	'',
	td = p.LastName,
	''
	FROM inserted
	JOIN Person p
	ON p.PersonID = INSERTED.[StudentID]
	FOR xml PATH ('tr'), TYPE)
	AS nvarchar(max))+
	N'<tbody></table>';

EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = @tableHTML,
	@subject = @subject,
	@body_format = 'HTML';

END
END
GO



insert into StudentGrade values(2021, 9, 0.20)
select * from StudentGrade

drop trigger email_lower_grade_than_min