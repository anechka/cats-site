window.startup = ->
  catsDataObject = window.catsDataObject

  collection = window.collection.map updateValues
  htmlBind = catsDataObject.innerHTML
  htmlResultProcessing = window.Plates.bind htmlBind, collection
  catsDataObject.innerHTML = htmlResultProcessing


window.updateValues = (incoming) ->

  # Забираем возраст из приходящего объекта
  catAge = incoming["cat.age"]

  # Если кот старше 11 месяцев, то превращаем его возраст в года
  if catAge > 11
    # делим возраст (в месяцах) на 12, и округляем до ближайшего целого числа
    catAge = Math.floor(catAge / 12)
    incoming["cat.age"] = catAge + " " + russian_str(catAge, "год", "года", "лет")
  else
    incoming["cat.age"] = catAge + " " + russian_str(catAge, "месяц", "месяца", "месяцев")
  catBillingPrice = incoming["cat.bill_in_day"]
  incoming["cat.bill_in_day"] = catBillingPrice + " " + russian_str(catBillingPrice, "рубль", "рубля", "рублей")
  incoming



russian_str = (i, str1, str2, str3) ->
  plural = (a) ->
    if a % 10 is 1 and a % 100 isnt 11
      0
    else if a % 10 >= 2 and a % 10 <= 4 and (a % 100 < 10 or a % 100 >= 20)
      1
    else
      2
  switch plural(i)
    when 0
      str1
    when 1
      str2
    else
      str3