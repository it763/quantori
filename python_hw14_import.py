import pickle
from  python_hw14_module import Employee
emp1=pickle.load( open( "import.tmp", "rb" ) )
emp1.print_salary_info()