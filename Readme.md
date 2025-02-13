# <b>API Docs</b>

API для взаимодействия с моделью бинарной классификации поступления абитуриентов на конкретное направление в ТИУ.

## Основные сущности:
### Applicant:
```
{  
  "year": int,  
  "gender": str,  
  "gpa": float,  
  "points": int,
  "direction": str
}
```

* year - год поступления абитуриента, принимает значения от 2019 до 2024.  

* gender - пол абитуриента ("М", "Ж").  

* gpa - средний балл атестата,  принимает значения от 3 до 5.  

* points - сумма баллов ЕГЭ, принимает значения от 0 до 310.  

* direction - название направления в ТИУ в формате "[Номер направления] [Название направления]".

 ## Основные методы:

>POST `/api/v1/model/applicant/`

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

 Пример ответа:
 ```
 {"probability": float}
 ````

 >POST `/api/v1/model/applicants/`

 Тело запроса:
 ```
 {
  "applicants": [
    {
      "year": 0,
      "gender": "М",
      "gpa": 0,
      "points": 0,
      "direction": "string"
    }
  ]
}
```

Пример ответа:
```
{"probabilities": List[float]}
```