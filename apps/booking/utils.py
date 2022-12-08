from apps.bio.models import UserProfile

from .tasks import send_details

from django.db.models import F, Func, Value, JSONField

# Thing.objects.update(
#     properties=Func(
#         F("properties"),
#         Value(["color"]),
#         Value("green", JSONField()),
#         function="jsonb_set",
#     )
# )


# thing = Thing.objects.get(name="...")
# thing.properties['color'] = 'green'
# thing.save()

def cashback(context, order, total_sum, company):
    user = context['request'].user
    profile = UserProfile.objects.get(user=user)
    company = str(company)

    if profile:
        # cashback = profile.values('cashback')[0]['cashback']
        cashback = profile.cashback #[str(company)]  # список словарей
        print('cash', cashback)
        if not cashback:
            reward = 0
            order.total_sum = total_sum
            collected_sum = total_sum
            cashback.append({company: {"cashback": 0, "collected_sum": collected_sum}})
            profile.save()
            # print('cash', cashback)
        else:
            for comp in cashback:
                if company in comp.keys():
                    print(comp)
                    print(company)
                    print(comp.keys())
                    reward = int(comp[company]['cashback'])
                    print(reward)
                    order.total_sum = total_sum - total_sum*reward/100
                    collected_summ = comp[company]['collected_sum']
                    comp[company]['collected_sum'] += order.total_sum
                    # collected_summ = int(profile.cashback[comp][company]['collected_sum'])
                    collected_summ += order.total_sum
                    # profile.cashback[comp][company]['collected_sum'] += order.total_sum
                    print(collected_summ)
                    print(type(collected_summ))

                    # check_cashback = int(cashback[company][cashback]) 
                    if collected_summ >= 10000:
                        comp[company]['cashback'] = 3
                        # profile.update(
                        #     cashback)  
                    if collected_summ >= 20000:
                        # profile.update(
                        #     cashback)
                        comp[company]['cashback'] = 5
                    if collected_summ >= 50000:
                        # profile.update(
                        #     cashback)
                        comp[company]['cashback'] = 7
                    if collected_summ >= 100000:
                        # profile.update(
                        #     cashback)
                        comp[company]['cashback'] = 10
                    # print(comp[company]['cashback'])
                    # print(type(comp[company]['cashback']))
                profile.save()
                print(profile.cashback)

        order.save()
        email = user.email
        print(email)
        code = order.code
        # print(code)
        send_details.delay(email, code)

        # print(collected_sum)

        # for comp in cashback:
        #     if comp['title'] == str(company):
        #         reward = int(comp['cashback'])
        #     else:
        #         cashback.append(
        #             {'company': str(company),
        #                         'cashback': 0, 
        #                         'collected_sum': 0}
        #                         )
        #         reward = 0
        
        # for comp in cashback:
        #     if company in comp.keys():
        #         reward = int(comp['cashback'])
        #     else:
        #         cashback.append({company: {'cashback': 0, 'collected_sum': 0}})
        #         reward = 0

            

            # collected_sum = int(cashback[company][collected_sum])
            # collected_sum += order.total_sum

            # print(collected_sum)


        # if profile:
        #     reward = int(cashback[cashback])
        # else:
        #     cashback.append({company: {cashback: 0, collected_sum: 0}})
        #     reward = 0

        # order.total_sum = total_sum - total_sum*reward/100

        # collected_sum = int(cashback[company][collected_sum])
        # collected_sum += order.total_sum

        # collected_sum = int(cashback[collected_sum])
        # cashback[collected_sum] += order.total_sum

        # profile.update(   # .setdefault(company, {cashback: 0, collected_sum: 0})
        #     cashback=Func(
        #         F(company),
        #         Value('collected_sum'),
        #         Value(collected_sum, JSONField()),
        #                 function="jsonb_set",)
        #     )

        # check_cashback = int(cashback[company][cashback]) 
        # if check_cashback >= 10000:
        #     profile.update(
        #         cashback)  # .setdefault(
        #             # company, {cashback: 3, collected_sum: 0}
        #             # )
        # if check_cashback >= 20000:
        #     profile.update(
        #         cashback)
        # if check_cashback >= 50000:
        #     profile.update(
        #         cashback)
        # if check_cashback >= 100000:
        #     profile.update(
        #         cashback)

        # if cashback['collected_sum'] >= 10000:
        #     cashback['cashback'] = 3  # .setdefault(
        #             # company, {cashback: 3, collected_sum: 0}
        #             # )
        # if cashback['collected_sum'] >= 20000:
        #     cashback['cashback'] = 5
        # if cashback['collected_sum'] >= 50000:
        #     cashback['cashback'] = 7
        # if cashback['collected_sum'] >= 100000:
        #     cashback['cashback'] = 10

        # profile.save()

        # title = tours.tour.title # tour
        # date = tours.date # tour
        # guide = tours.guide # tour
        # people_num = people # order

        # profile.save()
        # order.save()
        # email = user.email
        # code = order.code
        # # print(code)
        # send_details(email, code)

    
    if not profile:
        return 'Чтобы получить скидку, заполните свой профиль.'


# чтоб отнималось количество занятых мест
# проверки на количество свободынх мест

# отсюда вниз убрать в отдельный файл
    # reward = int(profile.values('cashback')[0]['cashback'])
    # order.total_sum = total_sum - total_sum*reward/100

    # collected_sum = int(profile.values('collected_sum')[0]['collected_sum'])
    # collected_sum += order.total_sum

    # profile.update(
    #     collected_sum=collected_sum)

    # check_cashback = int(profile.values('collected_sum')[0]['collected_sum']) 
    # if check_cashback >= 10000:
    #     profile.update(
    #         cashback=5)
    # if check_cashback >= 20000:
    #     profile.update(
    #         cashback=7)
    # if check_cashback >= 30000:
    #     profile.update(
    #         cashback=10)

    # user = self.context['request'].user
    #     profile = UserProfile.objects.filter(user=user)



    #     items = validated_data.pop('items')
    #     validated_data['user'] = self.context['request'].user
    #     order = super().create(validated_data) # Order.objects.create
    #     total_sum = 0
    #     orders_items = []
    #     for item in items:
    #         orders_items.append(OrderItems(
    #             order=order,
    #             book=item['book'],
    #             quantity=item['quantity']
    #         ))
    #         total_sum += item['book'].price * item['quantity']
    #     OrderItems.objects.bulk_create(orders_items, *args, **kwargs)

    #     reward = int(profile.values('cashback')[0]['cashback'])
    #     order.total_sum = total_sum - total_sum*reward/100

    #     collected_sum = int(profile.values('collected_sum')[0]['collected_sum'])
    #     collected_sum += order.total_sum

    #     profile.update(
    #         collected_sum=collected_sum)

    #     check_cashback = int(profile.values('collected_sum')[0]['collected_sum']) 
    #     if check_cashback >= 10000:
    #         profile.update(
    #             cashback=5)
    #     if check_cashback >= 20000:
    #         profile.update(
    #             cashback=7)
    #     if check_cashback >= 30000:
    #         profile.update(
    #             cashback=10)

    #     order.save()
    #     return order