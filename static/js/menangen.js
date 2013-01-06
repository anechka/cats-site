testingMonthes = function(incoming) {
    // Забираем возраст из приходящего объекта
    var catAge = incoming['cat.age'];
    // Если кот старше 11 месяцев, то превращаем его возраст в года
    if (catAge > 11) {
        // делим возраст (в месяцах) на 12, и округляем до ближайшего целого числа
        catAge = Math.floor(catAge/12)
        incoming['cat.age'] = catAge + " " + russian_str(catAge, 'год','года','лет')
    }

    else {
        incoming['cat.age'] = catAge + " " + russian_str(catAge, 'месяц','месяца','месяцев')
    }


    var catBillingPrice = incoming['cat.bill_in_day'];
    incoming['cat.bill_in_day'] = catBillingPrice + " " + russian_str(catBillingPrice, 'рубль','рубля','рублей')

    return incoming
}


function russian_str(i, str1, str2, str3){
    function plural (a){
        if ( a % 10 == 1 && a % 100 != 11 ) return 0
        else if ( a % 10 >= 2 && a % 10 <= 4 && ( a % 100 < 10 || a % 100 >= 20)) return 1
        else return 2;
    }

    switch (plural(i)) {
        case 0: return str1;
        case 1: return str2;
        default: return str3;
    }
}
