SELECT * FROM person; --person_id PK
PERSON_ID       FIRST_NAME      LAST_NAME       REMARKS                AGE
1               John            Doe             Does all the dishes    27
2               John            Doe             Walks the dogs         37
3               Jane            Doe             Hammers nail


select p1.person_id, p1.age, p2.age 
from person p1 
join person p2 on p1.age = p2.age 
-- left join person p2 on p1.age = p2.age 
-- where p2.age is NUll

shapes = [‘square’, ‘circle’, ‘triangle’, ‘rectangle’]
for shape in enumerate(shapes):
    print(shape)