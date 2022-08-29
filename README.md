# Music School

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

Welcome to our Music School! Many musicians apply to us every day, and we need you to create a model for it named `Musician`.

This model should have such fields:
* `first_name` — `CharField` with the `max_length` of 63;
* `last_name` — `CharField` with the `max_length` of 63;
* `instrument` — `CharField` with the `max_length` of 63;
* `age` — `IntegerField` (we **do not** accept people who are under 14);
* `date_of_applying` — `DateField` with `auto_now_add` parameter.

Implement the `__str__` method in this model to return the string in the `"first_name last_name"` form.

Also, we need to know whether the musician is an adult, so implement the `is_adult` property (an adult person is the one who is 21+). 
And last but not least, implement the most basic `CRUD` functionality!

**Please note:** the `is_adult` property should be displayed in the `GET` requests.
