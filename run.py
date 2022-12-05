from booking.booking import Booking
import booking.constants as const

with Booking() as bot:
    bot.land_first_page(constant=const)
    #bot.change_currency(currency='USD')
    bot.select_place_to_go(place_to_go='New York')
    bot.select_dates(check_in_date='2023-03-15',
        check_out_date='2023-03-25')
    bot.select_adults(adults=2)
    bot.complete_search()