def get_tuple_from_dict(d, param_list):
    result = ()
    for param in param_list:
        result = result + (d[param],)
    return result


def build_dict_epathshala(d):
    new_dict = {}
    new_dict["deviceid"] = d["deviceid"]
    new_dict["phoneno"] = d["phnum"]
    new_dict["udise"] = d["school"]
    new_dict["stuname"] = d["name"]
    new_dict["grade"] = d["grade"]
    new_dict["quizno"] = d["quiz_value"]
    new_dict["subject"] = "Hindi"
    new_dict["quizstatus"] = "C"
    new_dict["start"] = d["start"]
    new_dict["end"] = d["end"]
    new_dict["today"] = d["today"]
    if new_dict["grade"] == "3":
        new_dict["q1"] = d["ques_3_hindi_1_ans"]
        new_dict["q2"] = d["ques_3_hindi_2_ans"]
        new_dict["q3"] = d["ques_3_hindi_3_ans"]
        new_dict["q4"] = d["ques_3_hindi_4_ans"]
        new_dict["q5"] = d["ques_3_hindi_5_ans"]
        new_dict["q6"] = d["ques_3_maths_1_ans"]
        new_dict["q7"] = d["ques_3_maths_2_ans"]
        new_dict["q8"] = d["ques_3_maths_3_ans"]
        new_dict["q9"] = d["ques_3_maths_4_ans"]
        new_dict["q10"] = d["ques_3_maths_5_ans"]
    elif new_dict["grade"] == "4":
        new_dict["q1"] = d["ques_4_hindi_1_ans"]
        new_dict["q2"] = d["ques_4_hindi_2_ans"]
        new_dict["q3"] = d["ques_4_hindi_3_ans"]
        new_dict["q4"] = d["ques_4_hindi_4_ans"]
        new_dict["q5"] = d["ques_4_hindi_5_ans"]
        new_dict["q6"] = d["ques_4_maths_1_ans"]
        new_dict["q7"] = d["ques_4_maths_2_ans"]
        new_dict["q8"] = d["ques_4_maths_3_ans"]
        new_dict["q9"] = d["ques_4_maths_4_ans"]
        new_dict["q10"] = d["ques_4_maths_5_ans"]
    elif new_dict["grade"] == "5":
        new_dict["q1"] = d["ques_5_hindi_1_ans"]
        new_dict["q2"] = d["ques_5_hindi_2_ans"]
        new_dict["q3"] = d["ques_5_hindi_3_ans"]
        new_dict["q4"] = d["ques_5_hindi_4_ans"]
        new_dict["q5"] = d["ques_5_hindi_5_ans"]
        new_dict["q6"] = d["ques_5_maths_1_ans"]
        new_dict["q7"] = d["ques_5_maths_2_ans"]
        new_dict["q8"] = d["ques_5_maths_3_ans"]
        new_dict["q9"] = d["ques_5_maths_4_ans"]
        new_dict["q10"] = d["ques_5_maths_5_ans"]
    else:
        new_dict["q1"] = new_dict["q2"] = new_dict["q3"] = new_dict["q4"] = new_dict["q5"] = new_dict["q6"] = new_dict["q7"] = new_dict["q8"] = new_dict["q9"] = new_dict["q10"] = None
    new_dict["totmarks"] = d["total_score"]
    new_dict["maxmarks"] = 10
    new_dict["instance_id"] = d["instanceID"]
    return new_dict
