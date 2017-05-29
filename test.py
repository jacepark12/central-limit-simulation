# import paramiko
#
# key = paramiko.RSAKey.from_private_key_file('./yscholar_aws.pem')
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# transport = paramiko.Transport()
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# host = 'ec2-54-190-7-146.us-west-2.compute.amazonaws.com'
# print("connecting")
#
# client.connect(hostname=host, username='ubuntu', pkey=key)
#
# print('connected')
#
# print('deleting dist dir')
# commands = ['rm -rf /home/ubuntu/yscholar_front/db.kscy.org_Front/dist']
#
# for command in commands:
#     stdin , stdout, stderr = client.exec_command(command)
#     print(stdout.read())
#     print( "Errors")
#     print(stderr.read())
#
# local_path = './dist'
# remote_path = '/home/ubuntu/yscholar_front/db.kscy.org_Front/dist'
#
# sftp.put(localpath=local_path, remotepath=remote_path)
#
# print('closing connection...')
# sftp.close()
# transport.close()
#
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

n, p = 72, 1/3
ITERATE = 100000
datas = np. random.binomial(n, p, ITERATE)

v = []
for i in range(1, 73):
    v.append(0)

print(v)
print(len(v))

for data in datas:
    v[data - 1] += 1

print('data')
print(v)
print(len(v))


for i in range(1, 72):
    print('i : ', i)
    v[i] /= ITERATE

print(v)

sum = 0

for i in range(1, 72):
    print('i : ', i)
    sum = sum + v[i]

print(sum)

plt.figure(figsize=(7,7))
#stats.problot(v)
plt.plot(v)
plt.show()
import statsmodels.api as sm
from matplotlib import pyplot as plt
#data = sm.datasets.longley.load()
data = v
data.exog = sm.add_constant(data.exog)
mod_fit = sm.OLS(data.endog, data.exog).fit()
res = mod_fit.resid # residuals
fig = sm.qqplot(res)
plt.show()