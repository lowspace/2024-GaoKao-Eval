parameter is:
	{'lang': 'zh', 'sequential': 'process-first', 'cot': False, 'print_question': True}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 每一题都需要分三步进行解答，并打印每一步的结果：
	1. 打印当前解答题目的所有内容。包括题干，选项或者空格。
	2. 写出该题目的解答过程。
	3. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。

# 输出格式

## {题目的阿拉伯数字编号}

### 原题
{...}

***

### 解题过程
{...}

***

### 答案
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'process-first', 'cot': True, 'print_question': True}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 解答题目时需要使用思维链（Chain of Thought，CoT）逐步（step by step）进行解答。
- 每一题都需要分三步进行解答，并打印每一步的结果：
	1. 打印当前解答题目的所有内容。包括题干，选项或者空格。
	2. 写出该题目的解答过程。
	3. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。

# 输出格式

## {题目的阿拉伯数字编号}

### 原题
{...}

***

### 解题过程
{...}

***

### 答案
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'answer-first', 'cot': False, 'print_question': True}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 每一题都需要分三步进行解答，并打印每一步的结果：
	1. 打印当前解答题目的所有内容。包括题干，选项或者空格。
	2. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。
	3. 写出该题目的解答过程。

# 输出格式

## {题目的阿拉伯数字编号}

### 原题
{...}

***

### 答案
{...}

***

### 解题过程
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'answer-first', 'cot': True, 'print_question': True}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 解答题目时需要使用思维链（Chain of Thought，CoT）逐步（step by step）进行解答。
- 每一题都需要分三步进行解答，并打印每一步的结果：
	1. 打印当前解答题目的所有内容。包括题干，选项或者空格。
	2. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。
	3. 写出该题目的解答过程。

# 输出格式

## {题目的阿拉伯数字编号}

### 原题
{...}

***

### 答案
{...}

***

### 解题过程
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'process-first', 'cot': False, 'print_question': True}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- Each problem needs to be solved in three steps, and print the result of each step:
	1. Print all the content of the current problem, including the question, options, or blanks.
	2. Write the solution process for the problem.
	3. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.

# Output Format

## {problem number}

### Original Problem
{...}

***

### Solution Process
{...}

***

### Answer
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'process-first', 'cot': True, 'print_question': True}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- When solving the problems, use the Chain of Thought (CoT) to solve them step by step.
- Each problem needs to be solved in three steps, and print the result of each step:
	1. Print all the content of the current problem, including the question, options, or blanks.
	2. Write the solution process for the problem.
	3. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.

# Output Format

## {problem number}

### Original Problem
{...}

***

### Solution Process
{...}

***

### Answer
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'answer-first', 'cot': False, 'print_question': True}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- Each problem needs to be solved in three steps, and print the result of each step:
	1. Print all the content of the current problem, including the question, options, or blanks.
	2. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.
	3. Write the solution process for the problem.

# Output Format

## {problem number}

### Original Problem
{...}

***

### Answer
{...}

***

### Solution Process
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'answer-first', 'cot': True, 'print_question': True}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- When solving the problems, use the Chain of Thought (CoT) to solve them step by step.
- Each problem needs to be solved in three steps, and print the result of each step:
	1. Print all the content of the current problem, including the question, options, or blanks.
	2. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.
	3. Write the solution process for the problem.

# Output Format

## {problem number}

### Original Problem
{...}

***

### Answer
{...}

***

### Solution Process
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'process-first', 'cot': False, 'print_question': False}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 每一题都需要分两步进行解答，并打印每一步的结果：
	1. 写出该题目的解答过程。
	2. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。

# 输出格式

## {题目的阿拉伯数字编号}

### 解题过程
{...}

***

### 答案
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'process-first', 'cot': True, 'print_question': False}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 解答题目时需要使用思维链（Chain of Thought，CoT）逐步（step by step）进行解答。
- 每一题都需要分两步进行解答，并打印每一步的结果：
	1. 写出该题目的解答过程。
	2. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。

# 输出格式

## {题目的阿拉伯数字编号}

### 解题过程
{...}

***

### 答案
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'answer-first', 'cot': False, 'print_question': False}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 每一题都需要分两步进行解答，并打印每一步的结果：
	1. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。
	2. 写出该题目的解答过程。

# 输出格式

## {题目的阿拉伯数字编号}

### 答案
{...}

***

### 解题过程
{...}

***

```
parameter is:
	{'lang': 'zh', 'sequential': 'answer-first', 'cot': True, 'print_question': False}
prompt    is:
```
# 人设
请帮助我解答所有给定的数学题目。

# 策略
- 逐一解答给出的题目。
- 一次性解答完所有题目。
- 解答题目时需要使用思维链（Chain of Thought，CoT）逐步（step by step）进行解答。
- 每一题都需要分两步进行解答，并打印每一步的结果：
	1. 根据格式给出题目的答案。格式：
		- 选择题：`{'{题目的阿拉伯数字编号': [{答案}]}`，比如 `{'99': ['E']}`或者`{'98': ['E', 'F']}`。
		- 填空题：`{'{题目的阿拉伯数字编号': [{LaTex格式的答案}]}`，比如 `{'97': ['$0$']}`或者`{'96': ['$0$', '$1$']}`。
	2. 写出该题目的解答过程。

# 输出格式

## {题目的阿拉伯数字编号}

### 答案
{...}

***

### 解题过程
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'process-first', 'cot': False, 'print_question': False}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- Each problem needs to be solved in two steps, and print the result of each step:
	1. Write the solution process for the problem.
	2. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.

# Output Format

## {problem number}

### Solution Process
{...}

***

### Answer
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'process-first', 'cot': True, 'print_question': False}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- When solving the problems, use the Chain of Thought (CoT) to solve them step by step.
- Each problem needs to be solved in two steps, and print the result of each step:
	1. Write the solution process for the problem.
	2. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.

# Output Format

## {problem number}

### Solution Process
{...}

***

### Answer
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'answer-first', 'cot': False, 'print_question': False}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- Each problem needs to be solved in two steps, and print the result of each step:
	1. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.
	2. Write the solution process for the problem.

# Output Format

## {problem number}

### Answer
{...}

***

### Solution Process
{...}

***

```
parameter is:
	{'lang': 'en', 'sequential': 'answer-first', 'cot': True, 'print_question': False}
prompt    is:
```
# Persona
Please help me solve all the given math problems.

# Strategy
- Solve the given problems one by one.
- Solve all problems at once.
- When solving the problems, use the Chain of Thought (CoT) to solve them step by step.
- Each problem needs to be solved in two steps, and print the result of each step:
	1. Provide the answer to the problem in the format:
		- Multiple choice: `{'{question number}': [{answers}]}`, for example `{'99': ['E']}` or `{'98': ['E', 'F']}`.
		- Fill-in-the-blank: `{'{question number}': [{LaTex format answers}]}`, for example `{'97': ['$0$']}` or `{'96': ['$0$', '$1$']}`.
	2. Write the solution process for the problem.

# Output Format

## {problem number}

### Answer
{...}

***

### Solution Process
{...}

***

```
