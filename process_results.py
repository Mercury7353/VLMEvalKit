# 读取给定 .log文件
# 找到所有:
'''
  warnings.warn(
A/B/C/D

'''
#的pattern， 抽取出来，把这些字母存成一个列表
'''
然后按照顺序读取 /mnt/afs/zhangyaolun/.cache/huggingface/hub/datasets--honglyhly--WorldSense/snapshots/49df5aa9d62c4900bca7e86c3a9d476122e47fcc/worldsense_qa.json 里面的tasks
（注意，可能一个key下有多个task），根据给定answer和从log里面抽取出来的answer计算正确率
格式示例：
"dvOkwKAs": {
        "video_id": "dvOkwKAs",
        "video_duration": "60s",
        "duration": "<1min",
        "domain": "Music",
        "sub_category": "Covers",
        "audio_class": [
            "Music"
        ],
        "video_caption": "A young man and woman, both wearing white short-sleeved shirts, sit facing the camera playing guzhengs. The woman's shirt has a small logo on the chest and a red sash around her waist. They pluck the strings with picks attached to their right hands.\u00a0 The background features a wall with a colorful mural incorporating celestial and organic imagery.\u00a0 Behind the woman is a partially visible, closed metal gate.The camera pans to the right, revealing two more young women seated and playing guzhengs.\u00a0They wear similar white shirts, one with a light teal sash and the other with a red one. They too use picks on their right hands.  A staircase is partially visible in the background. The camera remains stationary as the four students continue to play.",
        "task0": {
            "task_domain": "Understanding",
            "task_type": "Spatial Relation",
            "question": "What is the position of the metal roller door relative to the woman wearing white in the video?",
            "answer": "B",
            "candidates": [
                "A. To the left of the woman wearing white.",
                "B. To the right of the woman wearing white.",
                "C. In front of the woman wearing white.",
                "D. Behind the woman wearing white."
            ]
        }
    },
    "UYkFSXsh": {
        "video_id": "UYkFSXsh",
        "video_duration": "119s",
        "duration": "1-2min",
        "domain": "Culture & Politics",
        "sub_category": "Politics",
        "audio_class": [
            "Speech",
            "Event"
        ],
        "video_caption": "The video begins with a light background and a logo at the top center. Below the logo is a youtube subscribe button. At the bottom of the screen is a text overlay. The video transitions to a scene that is bordered by a multi-colored frame. In the center of the screen is a man holding a microphone. There is a white backdrop behind him with text at the top, and there is a christmas tree on the right. A text banner along with several social media icons appears at the bottom of the video. The scene then changes to show an audience of people sitting. The scene then returns to the man speaking, and he gestures with his hands. He then points at the camera and continues talking. The camera then continues to focus on him as he gestures and talks. During this time a variety of banners appear at the bottom of the screen with different advertisements. The video then ends with a final scene of him standing and facing the camera.",
        "task0": {
            "task_domain": "Reasoning",
            "task_type": "Audio Change",
            "question": "At the end of the video, how did the volume of the man speaking in the black suit change, if at all?",
            "answer": "B",
            "candidates": [
                "A. It is unclear to me.",
                "B. The volume increased from soft to loud.",
                "C. The volume decreased from loud to soft."
            ]
        },
        "task1": {
            "task_domain": "Recognition",
            "task_type": "Temporal Localization",
            "question": "At what point in the video do the audience members cheer?",
            "answer": "D",
            "candidates": [
                "A. In the middle of the video.",
                "B. Throughout the video.",
                "C. At the end of the video.",
                "D. At the beginning of the video."
            ]
        }
    },
    "hHwdqJxc": {
        "video_id": "hHwdqJxc",
        "video_duration": "408s",
        "duration": "6-8min",
        "domain": "Tech & Science",
        "sub_category": "Engineering Projects",
        "audio_class": [
            "Speech",
            "Event"
        ],
        "video_caption": "The video contains 14 distinct clips that are stitched together.The first clip shows a person wearing a white hard hat with the text \"THIESS\" and the name \"PHIL\" printed on it, sunglasses, and an orange shirt with a white stripe. They appear to be standing in front of a large industrial construction site, with various metal structures, scaffolding, and equipment visible.  There are also orange safety cones on the ground.The second clip shows a person wearing a dark polo shirt with a red logo, and dark pants, standing in front of several garages with the text \"MARUSSIA F1 TEAM\" on them.  Multiple people and several racing cars can be seen in the garage.The third clip shows race cars entering pit stops. A race team is present, and appear to be working on the cars.  The first car is silver, the second is red and blue, the third is red, and the fourth is white and blue.The fourth clip shows the same person as in the second clip standing in the same location. A couple of other people appear in the background.The fifth clip shows a race car driving on a race track. People can be seen in the stands.The sixth clip shows a race car driving on a race track.The seventh clip shows the same person as in the second and fourth clips standing in the same location. Multiple people wearing orange uniforms appear in the background.The eighth clip shows the same person as in the second, fourth, and seventh clips standing in the same location.The ninth clip shows the same person as in the first clip wearing a plaid shirt, in front of a building with the text \"SCANIA\" on it.The tenth clip shows a person wearing a white hard hat with the text \"Schlumberger\" on it, safety glasses, and a blue uniform, standing in front of a white door and a gray wall, with various safety signs also visible.The eleventh clip shows the same person as in the ninth clip wearing a blue shirt, in front of a balcony. There are several buildings in the background.The twelfth clip shows the same person as in the first clip wearing a white hard hat, sunglasses, and an orange shirt in front of a body of water. There is construction equipment, and a partially constructed bridge visible.The thirteenth clip shows the same person as in the second, fourth, seventh and eighth clips wearing a red polo shirt with a black stripe on the side, standing in front of three framed pieces of wall art.The fourteenth clip shows four people standing together in front of a framed image of a vehicle.The fifteenth clip shows a person wearing a yellow safety vest and glasses in a car. A building and a road are visible in the background.The sixteenth clip shows a person wearing a gray hoodie against a plain white background.The seventeenth clip shows a person wearing a black jacket in front of a red staircase.The eighteenth clip shows a person with a beard, wearing a blue hoodie, against a plain orange background.The nineteenth clip shows a person wearing glasses in front of a tractor, followed by a brief shot of the same person in what appears to be a workshop, holding a piece of equipment. The clip concludes with a shot of the person working on two monitors, with a phone to the right of the monitors.The twentieth clip shows a person wearing a dark jacket and a white shirt, standing in front of a paved road, a tree, shrubs, and a modern building with an angular facade.The twenty-first clip shows a person wearing a white t-shirt, with a picture in the background, in a room, with a bed to the left and a dresser on the right.The twenty-second clip shows a person wearing a military uniform in front of a ship with the number \"150\" on its hull.",
        "task0": {
            "task_domain": "Recognition",
            "task_type": "Audio Counting",
            "question": "How many times does the woman's voice appear in the video?",
            "answer": "B",
            "candidates": [
                "A. One.",
                "B. Two.",
                "C. Four.",
                "D. Three."
            ]
        }
    },

'''
import re
import json

    
import re

def extract_answers_from_log(log_path):
    with open(log_path, 'r') as f:
        log_text = f.read()
    # 按照每段以 xxxit 开头来切分日志
    parts = re.split(r'(?=\d+it \[)', log_text)

    answers = []

    for part in parts:
        # 匹配整行、无缩进、只有 A/B/C/D
        matches = re.findall(r'^(A|B|C|D)$', part, flags=re.MULTILINE)

        if len(matches) == 1:
            answers.append(matches[0])
    print(len(answers))
    print(len(parts))
    return answers


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
    log_file = "/mnt/afs/zhangyaolun/safe_model/sft_qwen_omni/VLMEvalKit_ForOmni/VLMEvalKit/qwenomni_worldsense_noframe0427_8nodes.log"  # 替换为你的 .log 文件路径
    json_file = "/mnt/afs/zhangyaolun/.cache/huggingface/hub/datasets--honglyhly--WorldSense/snapshots/49df5aa9d62c4900bca7e86c3a9d476122e47fcc/worldsense_qa.json"

    predictions = extract_answers_from_log(log_file)
    ground_truths = extract_tasks_from_json(json_file)
    compute_accuracy(predictions, ground_truths)
