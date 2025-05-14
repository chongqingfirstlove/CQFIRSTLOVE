from data_preprocessing import preprocess_data

from model_training import AdaboostBP

import joblib



def main():

    file_path = 'ST企业和非ST企业的合并.xlsx'

    label_column = '企业类型代码'



    # 预处理数据

    X, y, scaler = preprocess_data(file_path, label_column=label_column)



    # 训练模型

    model = AdaboostBP(n_estimators=10)

    model.fit(X, y)



    # 保存模型和标准化参数

    joblib.dump(model, 'bp_adaboost_model.pkl')

    joblib.dump(scaler, 'standard_scaler.pkl')



if __name__ == "__main__":

    main()