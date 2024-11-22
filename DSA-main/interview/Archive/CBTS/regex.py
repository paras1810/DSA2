#00852f3e-ff85
import re

if __name__ == "__main__":
    input_string = '00852f3e-ff85'
    #re.matchall('[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}')
    matches = re.findall('[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}', input_string)

    # Print matches
    print("Matches found:")
    for match in matches:
        print(match)


#Select row_num(n) from (Select salary from user_table order by salary asc);

# SELECT *
# FROM employee_table
# WHERE employment_type = 'salaried'
# ORDER BY hire_date
# LIMIT 1 OFFSET n - 1;

#dens_rank