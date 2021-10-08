import smtplib
from email.message import EmailMessage
import time

print(time.strftime("%X"))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("aarryyyadav@gmail.com", 'onerker@#Q1')
    with open('emailid2.txt', 'r') as f:
        data = f.read()
        # print(data)
        # print(type(data))
        for var in data.split(','):
            # print(str(var))
            msg = EmailMessage()
            msg['To'] = var
            msg['subject'] = ' Invitation to participate in the Online event "ENLIGHTENMENT" on 5th - 6th October 2021.'
            msg['From'] = 'priyanshugarg.it24@jecrc.ac.in'
            msg.add_alternative("""\
            <html>
                <head>
                    <style>
                        #points{
                            color:Blue;
                            font-weight:bold;
                        }
                        #ending{
                            color:rgb(61, 43, 43);
                            font-weight:bold;
                        }
                    </style>
                </head>
                <body>
                    Respected Sir/Mam,<br><br>
                    
                    Greetings from Spiritual Research Cell- A Rajyogya thought laboratory of Jaipur Engineering College and Research Centre, Jaipur.<br><br>
                    We hope you and your family are staying safe and thriving well!<br><br>
                    
                    We at Spiritual Research Cell firmly believe that the true awakening takes place from within and so, to revive your spirits and consecrate your minds, we've got the fuel! We feel privileged in presenting to you 𝑬𝑵𝑳𝑰𝑮𝑯𝑻𝑬𝑵𝑴𝑬𝑵𝑻, 𝑬𝒎𝒑𝒐𝒘𝒆𝒓 𝒚𝒐𝒖 𝒇𝒐𝒓 𝒚𝒐𝒖𝒓𝒔𝒆𝒍𝒇! - A two-day online event where prominent change-makers and distinguished individuals will share their insights of how to lead a sanguine life.<br><br>
                    
                    Join us on this voyage of skill and value enhancement and be a part of the best you can get in 2021!<br><br>
                    
                    <div id='points'>Take-Aways-<br>
                    Reinvent Yourself<br>
                    Meditation Techniques<br>
                    Positive Personality<br>
                    Key to Inner treasures<br>
                    Work-Life Balance<br>
                    Overcoming Adversities<br><br></div>
                    
                    Date: 5th & 6th October 2021<br>
                    Time : 10:00-11:30PM & 12:00-01:30 PM<br><br>
                    
                    <b>Registration Link:</b><br> 
                    <a href='https://forms.gle/ptvV9vy83C2ZG4DN8' target='_blank'>https://forms.gle/ptvV9vy83C2ZG4DN8</a><br><br>
                    
                    <b>So, let us all step out of faith and walk into our purpose!</b><br><br>
                    
                    <img src='https://lh3.googleusercontent.com/mayx7EoV0EeNr4FkWFWxhRfZziDLjOnZfLE-j3qaYJrdwwu9YuLmX4R9cqdo_HfN4xqjObazwQ8GwXYYa337bg72hXAZfHh0vjj4u-qobcEoAvtgZTg2FtgDO72YlL5uyArKBAW5=s0' height='624' width='624'>
                    <br><br>
                    <div id='ending'>
                    Thanks and Regards,<br>
                    Aryan Yadav,<br>
                    Coordinator, SRC<br>
                    Rajyoga Thought  Lab,<br>
                    JECRC, Jaipur<br>
                    </div><br>
                    <img src="https://ci5.googleusercontent.com/proxy/m9GGXFVp3nmOFo5mkqSUpuDYYpS6FfsVpWCcD-SnYzdRs8O465OF0296ThrOB7xFm-Tbc5LnUGO57T8ofw=s0-d-e1-ft#http://sws.jecrcuniversity.edu.in/1994.gif" class="CToWUd"><br>
                </body>
            </html>
            """, subtype='html')

            with open('firstattachment.jpeg', 'rb') as f:
                fileData = f.read()
                fileType = 'jpeg'
                # print(fileType)
                file_name = f.name
                # print(file_name)
                # print(fileType)
            msg.add_attachment(fileData, maintype='image', subtype=fileType, filename=file_name)

            with open('secondattachment.pdf', 'rb') as f:
                fileData = f.read()
                fileType = 'octet-stream'
                # print(fileType)
                file_name = f.name
                # print(file_name)
                # print(fileType)
            msg.add_attachment(fileData, maintype='application', subtype=fileType, filename=file_name)
            smtp.send_message(msg)
            print(f"{var}")

print(time.strftime("%X"))
#priyanshu2859@gmail.com
# msg['To'] = "aarryyyadav@gmail.com"
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login("praveengoliya420@gmail.com", 'qgrprovkdrmurqem')
#     smtp.send_message(msg)
#     print("done")