-- Configurations for sql email service.
use master 
go 
sp_configure 'show advanced options',1 
go 
reconfigure with override 
go 
sp_configure 'Database Mail XPs',1 
go 
reconfigure 
go 
sp_configure 'xp_cmdshell',1 
go 
reconfigure 
go

-- Configurations for sql email service.
IF NOT EXISTS(SELECT * FROM msdb.dbo.sysmail_profile WHERE  name = 'gmail')  
  BEGIN 
    --CREATE Profile [gmail] 
    EXECUTE msdb.dbo.sysmail_add_profile_sp 
      @profile_name = 'gmail', 
      @description  = 'gmail account for email notifications'; 
  END


-- Configurations for sql email service.
  IF NOT EXISTS(SELECT * FROM msdb.dbo.sysmail_account WHERE  name = 'gmail') 
  BEGIN 
    EXECUTE msdb.dbo.sysmail_add_account_sp 
    @account_name            = 'gmail', 
    @email_address           = 'sfinkel@integralytic.com',
    @replyto_address         = 'sfinkel@integralytic.com',
    @description             = '',
    @mailserver_name         = 'smtp.gmail.com', 
    @mailserver_type         = 'SMTP', 
    @port                    = '587', 
    @username                = 'sfinkel@integralytic.com',
    @password                = 'kikmlhxgsockpzkl',  
    @use_default_credentials =  0 , 
    @enable_ssl              =  1 ; 
  END 

-- Configurations for sql email service. 
  IF NOT EXISTS(SELECT *  
              FROM msdb.dbo.sysmail_profileaccount pa 
                INNER JOIN msdb.dbo.sysmail_profile p ON pa.profile_id = p.profile_id 
                INNER JOIN msdb.dbo.sysmail_account a ON pa.account_id = a.account_id   
              WHERE p.name = 'gmail' 
                AND a.name = 'gmail')  
  BEGIN 
    EXECUTE msdb.dbo.sysmail_add_profileaccount_sp 
      @profile_name = 'gmail', 
      @account_name = 'gmail', 
      @sequence_number = 1 ; 
  END 


-- Sending a simple email in sql.
EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = 'Hi Shoshi, Have a gr8 day:)',
	@subject = 'Test sql email';
	


-- Sending a query result email in sql.
SELECT oc.Location ,c.Title, p.LastName, p.FirstName
FROM Course c
JOIN OnsiteCourse oc
ON c.CourseID = oc.CourseID
JOIN  CourseInstructor ci
ON ci.CourseID = c.CourseID
JOIN Person p
ON p.PersonID = ci.PersonID;


SELECT
	CAST((SELECT 
	td = oc.Location,
	'',
	td = c.Title,
	'',
	td = p.LastName,
	'',
	td = p.FirstName,
	''
	FROM Course c
	JOIN OnsiteCourse oc
	ON c.CourseID = oc.CourseID
	JOIN  CourseInstructor ci
	ON ci.CourseID = c.CourseID
	JOIN Person p
	ON p.PersonID = ci.PersonID 
	FOR xml PATH ('tr'), TYPE)
	AS nvarchar(max));


DECLARE @tableHTML NVARCHAR(MAX);
SET @tableHTML = 
	N'<h1>Courses report</h1>'+
	N'<table border="1" style="border-collapse: collapse; width: 100%; background: #F5F5F5; background: linear-gradient(to bottom, #FFFFFF, #F0F0F0)">'+
	N'<tr><thead><th style="background-color: #0000FF; color: white">Location</th><th style="background-color: #FF0000; color: white">Subject</th><th style="background-color: #FFFF00; color: black">LastName</th><th style="background-color: #00FF00; color: black">FirstName</th></thead><tbody>'+
	CAST((SELECT 
	td = oc.Location,
	'',
	td = c.Title,
	'',
	td = p.LastName,
	'',
	td = p.FirstName,
	''
	FROM Course c
	JOIN OnsiteCourse oc
	ON c.CourseID = oc.CourseID
	JOIN  CourseInstructor ci
	ON ci.CourseID = c.CourseID
	JOIN Person p
	ON p.PersonID = ci.PersonID 
	FOR xml PATH ('tr'), TYPE)
	AS nvarchar(max))+
	N'<tbody></table>';

EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'gmail',
	@recipients = 'sfinkel@integralytic.com',
	@body = @tableHTML,
	@subject = 'Instructor Locations Report',
	@body_format = 'HTML';
