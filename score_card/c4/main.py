# Coding : utf-8
# Author : chyh
# Date   : 2021/5/29 12:15

import pandas as pd
import os
import matplotlib.pyplot as plt


def data_read(data_path, file_name):
    df = pd.read_csv(os.path.join(data_path, file_name), delim_whitespace=True, header=None)
    # 变量重命名
    columns = ['status_account', 'duration', 'credit_history', 'purpose', 'amount',
               'saving_account', 'present_emp', 'income_rate', 'personal_status',
               'other_debtors', 'residence_info', 'property', 'age',
               'inst_plans', 'housing', 'num_credits',
               'job', 'dependents', 'telephone', 'foreign_worker', 'target']
    df.columns = columns
    # 将标签变量由状态1,2转为0,1;0表示好用户，1表示坏用户
    df.target = df.target - 1
    return df


# 离散变量与连续变量区分
def category_continue_separation(df):
    categorical_var = []
    numerical_var = []
    feature_names = list(dataframe)
    if 'target' in feature_names:
        feature_names.remove('target')
    # 先判断类型，如果是int或float就直接作为连续变量
    numerical_var = list(df[feature_names].select_dtypes(
        include=['int', 'float', 'int32', 'float32', 'int64', 'float64']).columns.values)
    categorical_var = [x for x in feature_names if x not in numerical_var]
    return categorical_var, numerical_var


# 数据初步分析
def describe(df):
    categorical_var, numerical_var = category_continue_separation(df)
    print(df[numerical_var].describe())


def show_abnormal(df):
    # 对于连续数据绘制箱线图，观察是否有异常值
    categorical_var, numerical_var = category_continue_separation(df)
    plt.figure(figsize=(10, 6))  # 设置图形尺寸大小
    for j in range(1, len(numerical_var) + 1):
        plt.subplot(2, 4, j)
        df_temp = df[numerical_var[j - 1]][~df[numerical_var[j - 1]].isnull()]
        plt.boxplot(df_temp,
                    notch=False,  # 中位线处不设置凹陷
                    widths=0.2,  # 设置箱体宽度
                    medianprops={'color': 'red'},  # 中位线设置为红色
                    boxprops=dict(color="blue"),  # 箱体边框设置为蓝色
                    labels=[numerical_var[j - 1]],  # 设置标签
                    whiskerprops={'color': "black"},  # 设置须的颜色，黑色
                    capprops={'color': "green"},  # 设置箱线图顶端和末端横线的属性，颜色为绿色
                    flierprops={'color': 'purple', 'markeredgecolor': "purple"}  # 异常值属性，这里没有异常值，所以没表现出来
                    )
    plt.show()


if __name__ == '__main__':
    dataframe = data_read("data", "german.csv")
    # print(dataframe)
    # print(category_continue_separation(dataframe))
    # describe(dataframe)
    show_abnormal(dataframe)