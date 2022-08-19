# Music School

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before start.

Welcome to our Music School.
A lot of musicians apply to us every day and we need you to create model for it named `Musician`.

This model should have such fields:
* `first_name` — `CharField` with the `max_length` of 64;
* `last_name` — `CharField` with the `max_length` of 64;
* `instrument` — `CharField` with the `max_length` of 64;
* `age` - `IntegerField` (we **do not** accept people who are under 14);
* `date_of_applying` - `DateField` with `auto_now_add` parameter.

Implement the `__str__` method in this model, so it should return: `"first_name last_name"`.

Also, we need to know whether the musician is adult, so implement the `is_adult` property (adult person is the one who is 21+).
And last but not least, make all CRUD work!

**Please note:** `is_adult` property should be displayed in GET requests.
