import json  

def parse_resume(resume_text):  
     
    lines = resume_text.strip().split('\n')  
    
    resume_data = {  
        "name": "",  
        "contact_info": {},  
        "education": [],  
        "experience": []  
    }  

    resume_data["name"] = lines[0].strip()  
    resume_data["contact_info"]["email"] = lines[1].split(":")[1].strip()  
    resume_data["contact_info"]["phone"] = lines[2].split(":")[1].strip()  

    education_started = False  
    experience_started = False  
    for line in lines[3:]:  
        line = line.strip()  
        if line.startswith("Education:"):  
            education_started = True  
            continue  
        if line.startswith("Experience:"):  
            experience_started = True  
            education_started = False  
            continue  

        if education_started and line:  
            resume_data["education"].append(line)  
        elif experience_started and line:  
            resume_data["experience"].append(line)  

    return resume_data  

# Example Resume Text  
resume_text = """\
Akrati Rathore  
Email: akrati1@gmail.com  
Phone: 1234567890  
Education:  
B.tech. in Computer Science GLA University (2025)  
Experience:  
Software Engineer at XYZ company  
"""  

# Parse the resume and convert to JSON  
parsed_resume = parse_resume(resume_text)  
json_output = json.dumps(parsed_resume, indent=4)  

print(json_output)  

# Optional: Save to a file  
with open("resume.json", "w") as json_file:  
    json_file.write(json_output)