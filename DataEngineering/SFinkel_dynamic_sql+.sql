DECLARE @sum_credits NVARCHAR(10),
		@student_id NVARCHAR(10),
		@sql NVARCHAR(MAX),
		@message NVARCHAR(500),
		@student NVARCHAR(MAX),
		@subject NVARCHAR(100);

SET @student_id = 6

SET @sql = 'SELECT @credits = SUM(c.Credits)
FROM Course c
JOIN StudentGrade sg
ON c.CourseID = sg.CourseID
WHERE sg.StudentID = ' + @student_id+';'

EXEC sp_executesql @sql, N'@credits NVARCHAR(MAX) OUTPUT', @credits = @sum_credits OUTPUT;

SET @sql = 'SELECT @name = FirstName +'' ''+LastName
FROM Person
WHERE PersonID = '+@student_id+';'

EXEC sp_executesql @sql, N'@name NVARCHAR(MAX) OUTPUT', @name = @student OUTPUT;

IF @sum_credits IS NULL

BEGIN
SET @message = N'<H2>Credits For Student '+@student_id+'</H2>'
			+'<H3>'+@student +' did not pass any courses yet.</H3>';
END

ELSE
BEGIN
SET @message = N'<H2>Credits For Student '+@student_id+'</H2>'
			+'<H3>The total credits for '+@student +' is '+@sum_credits+ '.</H3>';
END

SET @subject = 'Credits for '+ @student 

EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = @message,
	@subject = @subject,
	@body_format = 'HTML';


-- Assigment2
DECLARE @department_id NVARCHAR(10),
		@sql1 NVARCHAR(MAX),
		@table_output NVARCHAR(MAX),
		@email_body NVARCHAR(MAX),
		@email_subject NVARCHAR(100);

SET @department_id = 2;

SET @sql1 = 'SET @table_result = 
			''<br/>
			<html><body><H1>Courses in Department '+@department_id+'</H1>
			<table border = "1">
			<tr><th>Title</th>
				<th>Credits</th>
				<th>Department</th></tr> ''+
			CAST((SELECT td = c.Title, '''',
						td = c.Credits, '''',
						td = d.Name, ''''
					FROM Course c
					JOIN Department d
					ON c.DepartmentID = d.DepartmentID
					WHERE c.DepartmentID = '+@department_id+'
					FOR XML PATH(''tr''), ELEMENTS) AS NVARCHAR(MAX)) +
					''</table></body></html>'''

EXEC sp_executesql @sql1, N'@table_result NVARCHAR(MAX) OUTPUT', @table_result = @table_output OUTPUT;
SET @email_body = @table_output;
SET @email_subject = 'Courses in department '+@department_id


EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = @email_body,
	@subject = @email_subject,
	@body_format = 'HTML';










