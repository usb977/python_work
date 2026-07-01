from datetime import time,datetime,timedelta

prompt_come_hour = "请输入您上班时刻的h："
prompt_come_min = "请输入您上班时刻的min："
prompt_leave_hour = "请输入您下班时刻的h："
prompt_leave_min = "请输入您下班时刻的min："

while True:
    print("任何时候输入'q'即可退出程序！")
    come_hour = input(prompt_come_hour)
    if come_hour == 'q':
        break
    come_min = input(prompt_come_min)
    if come_min == 'q':
        break
    leave_hour = input(prompt_leave_hour)
    if leave_hour == 'q':
        break
    leave_min = input(prompt_leave_min)
    if leave_min == 'q':
        break

    t_come = time(int(come_hour),int(come_min),0)
    t_leave = time(int(leave_hour),int(leave_min),0)
    dt1 = datetime(2026,1,1, t_come.hour, t_come.minute, t_come.second)
    dt2 = datetime(2026,1,1, t_leave.hour, t_leave.minute, t_leave.second)- timedelta(hours=1, minutes=30, seconds=0)
    delta = dt2 - dt1
    print(f"\n您今天的总工作时长为：{delta}")