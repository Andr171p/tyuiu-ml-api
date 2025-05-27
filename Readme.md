# Классификация поступления на бюджет

##  <b>API</b>

> POST `/api/v1/classifier/predict`

Тело запроса:
```
{
  "year": 0,
  "gender": "М",
  "gpa": 0,
  "points": 0,
  "direction": "string"
}
```

* <b>year</b> - год поступления абитуриента, принимает значения от 2019 до 2024.
* <b>gender</b> - пол абитуриента Literal["male", "female"].
* <b>gpa</b> - средний балл аттестата,  принимает значения от 3 до 5.
* <b>points</b> - сумма баллов ЕГЭ, принимает значения от 0 до 310.
* <b>direction</b> - Наименование направления подготовки.

Тело ответа:
```json
{
  "direction": "string",
  "probability": 0
}
```

> POST `/api/v1/classifier/predict-batch`

Тело запроса:
```json
{
  "applicants": [
    {
      "year": 2019,
      "gender": "male",
      "gpa": 3,
      "points": 310,
      "direction": "string"
    }
  ]
}
```
Тело ответа:
```json
[
  {
    "direction": "string",
    "probability": 0
  }
]
```