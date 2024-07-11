import json
import os

import .parse_data

def gen_single_turn_prompt(questions = [], lang = 'zh', ques_idx = '1') -> str:
