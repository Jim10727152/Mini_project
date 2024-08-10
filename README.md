# Mini_project


This is Jim, welcome !

##############################################################################################################

Centralized learning !!!

1.Data_preprocessing.ipynb is used to turn the original 'FL-Event-Filtered.csv' into preprocessed_data.csv.

2.Then the preprocessed_data can be the input of xgboost model or nn model.

##############################################################################################################

　　 へ　　　　　／|
　　/＼7　　∠＿/
　 /　│　　 ／　／
　│　Z ＿,＜　／　　 /`ヽ
　│　　　　　ヽ　　 /　　〉
　 Y　　　　　`　 /　　/
　ｲ●　､　●　　⊂⊃〈　　/
　()　 へ　　　　|　＼〈
　　>ｰ ､_　 ィ　 │ ／／
　 / へ　　 /　ﾉ＜| ＼＼
　 ヽ_ﾉ　　(_／　 │／／
　　7　　　　　　　|／
　　＞―r￣￣`ｰ―＿


##############################################################################################################

For federated learning model, please click the directory 'flr_fed' and then open 4 terminal

The first  terminal : execute 'python flr_server.py'
The second terminal : execute 'python flr_client.py --csv Client1_data.csv'
The third  terminal : execute 'python flr_client.py --csv Client2_data.csv'
The forth  terminal : execute 'python flr_client.py --csv Client3_data.csv'

wait for about 30 seconds , you will see the result in the terminal of the server.
