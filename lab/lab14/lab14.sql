create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;


-- Pizza places that open before 1pm in alphabetical order
CREATE TABLE opening AS
SELECT  name
FROM pizzas
WHERE open < 13
AND close >= 13
ORDER BY name DESC;


-- Two meals at the same place
CREATE TABLE double AS
SELECT  first.meal
       ,second.meal
       ,pizza.name
FROM meals AS first, meals AS second, pizzas AS pizza
WHERE second.time - first.time > 6
AND pizza.open <= first.time
AND pizza.close >= second.time;

