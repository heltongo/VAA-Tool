FILE_DIR = os.path.dirname(os.path.realpath(CrashStatisticsVictoria.csv))


def read_csv(CrashStatisticsVictoria.csv):
    """
    Creates a generator to improve memory usage
    :param file_name:
    :return:
    """
    for row in open(os.path.join(CRASH_DATA, 'data', file_name), "r"):
        yield row
        print(row)

'''
# In[3]:


CrashFile = pd.read_csv(r"CrashStatisticsVictoria.csv")
CrashFile


# In[4]:


#solution1: date selection
def acc_date(start_date, end_date):
    Accident_date_df = CrashFile[CrashFile["ACCIDENT_DATE"].between(start_date,end_date)] 
    return Accident_date_df

acc_date_values = acc_date('1/7/2017','1/7/2019')
acc_date_values


# In[5]:


#solution:3 -- keyword selection analysis
def acc_type(start_date, end_date,keyword):
    abc=acc_date(start_date, end_date)
    Accident_type_df = abc[abc["ACCIDENT_TYPE"].str.contains(keyword, case = False)]
   
    return Accident_type_df

acc_type('1/7/2017','1/7/2019',"pedes")


# In[8]:


#solution 2 - hour selection

test1= CrashFile['ACCIDENT_TIME'].apply(lambda s: int(s.split('.')[0]))
test2 = test1.to_frame()
test2['index'] = test2.index
test3 = test2.groupby('ACCIDENT_TIME').count()
test3['Hour'] = test3.index

list1=list(test3['index'])
list2=list(test3['Hour'])

plt.xticks(range(1, 24))
plt.xlabel('Hourly analysis')
plt.ylabel('Number of accidents')
plt.plot(list2,list1)
plt.show()


# In[9]:


#solution 2 - hour selection with function, changes the y-axis to exponents instead of counts
def acc_hour(start_date, end_date):
    abc=acc_date(start_date, end_date)
    test1= abc['ACCIDENT_TIME'].apply(lambda s: int(s.split('.')[0]))
    test2 = test1.to_frame()
    test2['index'] = test2.index
    test3 = test2.groupby('ACCIDENT_TIME').count()
    test3['Hour'] = test3.index

    list1=list(test3['index'])
    list2=list(test3['Hour'])
    
    plt.xticks(range(1, 24))
    plt.xlabel('Hourly analysis')
    plt.ylabel('Number of accidents')
    plt.plot(list2,list1)
    plt.show()
    
acc_hour('1/7/2017','1/7/2019')


# In[ ]:

'''


