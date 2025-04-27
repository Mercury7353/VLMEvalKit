
import re
import json

    
import re

def extract_question_content(log_path):
    with open(log_path, 'r') as f:
        log_text = f.read()
    # 按照每段以 xxxit 开头来切分日志
    #parts = re.split(r'(?=\d+it \[)', log_text)
    parts = log_text.split("\n")
    q = []
    print(len(parts))
    for part in parts:
        if "Check Messages " in part:
            q.append(part.split("Check Messages ")[-1])
    print("Sample:..",q[0])
    return q


def extract_tasks_from_json(json_path):
    """
    从 JSON 文件中提取所有任务的标准答案。
    返回一个答案列表。
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    gt_answers = []  # ground truth
    for video_id, video_data in data.items():
        for key in video_data:
            if key.startswith("task") and isinstance(video_data[key], dict):
                gt_answers.append(video_data[key].get("answer"))
    print(f"共提取 {len(gt_answers)} 个标准答案")
    return gt_answers

def compute_accuracy(predictions, ground_truths):
    """
    计算预测答案与标准答案的准确率。
    """
    min_len = min(len(predictions), len(ground_truths))
    correct = sum(p == g for p, g in zip(predictions[:min_len], ground_truths[:min_len]))
    accuracy = correct / min_len if min_len > 0 else 0
    print(f"正确数量: {correct}/{min_len}, 准确率: {accuracy:.2%}")
    return accuracy

if __name__ == "__main__":
    log_file = "/mnt/afs/zhangyaolun/safe_model/sft_qwen_omni/VLMEvalKit_ForOmni/VLMEvalKit/worldsense_qwen2vl_7B_8frame.log"  # 替换为你的 .log 文件路径
    json_file = "/mnt/afs/zhangyaolun/.cache/huggingface/hub/datasets--honglyhly--WorldSense/snapshots/49df5aa9d62c4900bca7e86c3a9d476122e47fcc/worldsense_qa.json"
    import ast

    questions = extract_question_content(log_file)
    print("提取了",len(questions),"个问题")
    with open("worldsense_qa.jsonl",'w') as f:
        for q in questions:
            data = ast.literal_eval(q)
            f.write(json.dumps(data) + '\n')
