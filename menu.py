#!/usr/bin/python3
# -*- coding: utf-8 -*-

#This script displays the menu interface for several kalin options
import units
import dataread as dr

def print_main_menu():
    print('\n \n')
    print('***Main menu***')
    print('------------------')
    print()
    print('[u] ===> Units')
    print('[f] ===> Format')
    print('[q/Q] ===> Exit menu\n')


def units_main_menu():
    print()
    print()
    print('***Units menu***')
    print('------------------')
    print('List of units:')
    print()
    print('[t] ==> Time')
    print('[l] ==> Length')
    print('[m] ==> Mass')
    print('[q/Q] ===> Exit menu\n')  


def time_units_menu():
    print()
    print()
    print('***List of time units***')
    print('------------------')
    print('[s/S] ==> seconds [s]')
    print('[h/H] ==> hours [hr]')
    print('[d/D] ==> days [days]')
    print('[y/Y] ==> years [yr]')
    print('[o/O] ==> other\n')


def length_units_menu():
    print()
    print()
    print('***List of length units***')
    print('------------------')
    print('[c/C] ==> centimeters [cm]')
    print('[m/M] ==> meters [m]')
    print('[r/R] ==> Rsun [Rsun]')
    print('[a/A] ==> AU [AU]')
    print('[o/O] ==> other\n')


def mass_units_menu():
    print()
    print()
    print('***List of mass units***')
    print('------------------')
    print('[g/G] ==> grams [g]')
    print('[k/K] ==> kilograms [kg]')
    print('[m/M] ==> Msun [Msun]')
    print('[o/O] ==> other\n')



def run_main_menu(Data, Columns):
    print_main_menu()
    option = input('Enter your option: ')
    while option != 'q': 
        if option == 'u':
            # Enter units menu 
            run_units_menu(Data, Columns)
        elif option == 'f':
            # Enter plot format menu 
            print('Format option has been called')
        else:
            print()
            print('ERROR: Invalid option.')
    
        print()
        print_main_menu()
        option = input('Enter your option: ')


def run_units_menu(Data, Columns):
    units_main_menu()
    option= input('Enter your option: ')
    while option != 'q': 
        if option == 't':
            print('List of variables: \n')
            for i in enumerate(Data[0]):
                print(str(i[0]+1) + ')',i[1])
            print()
 
            key = input('Select variable to convert (Default=1): ') or '0'
            if int(key) > 0:
                key = str(int(key) - 1) 
            time_units_menu()
            
            option_units = input('Select unit (Default=None): ' or 'N')
            if option_units == 'n' or option_units == 'N':
                pass
            elif option_units == 's' or option_units == 'S':
                Columns.update({key: [Columns[key][0], units.ptu]})
            elif option_units == 'h' or option_units == 'H':
                Columns.update({key: [Columns[key][0], units.hours]})
            elif option_units == 'd' or option_units == 'D':
                Columns.update({key: [Columns[key][0], units.days]})
            elif option_units == 'y' or option_units == 'Y':
                Columns.update({key: [Columns[key][0], units.yrs]})
            elif option_units == 'o' or option_units == 'O':
                new_unit = float(int('New unit (variable * new unit): '))
                Columns.update({key: [Columns[key][0], new_unit]})
            else:
                print('ERROR: Invalid option.')
 
        elif option == 'l':
            print('List of variables: \n')
            for i in enumerate(Data[0]):
                print(str(i[0]+1) + ')',i[1])
            print()
 
            key = input('Select variable to convert (Default=1): ') or '0'
            if int(key) > 0:
                key = str(int(key) - 1) 

            length_units_menu()
            
            option_units = input('Select unit (Default=Rsun): ')
            if option_units == 'r' or option_units == 'R':
                Columns.update({key: [Columns[key][0], 1]})
            elif option_units == 'c' or option_units == 'C':
                Columns.update({key: [Columns[key][0], units.pdu]})
            elif option_units == 'h' or option_units == 'M':
                Columns.update({key: [Columns[key][0], units.mts]})
            elif option_units == 'a' or option_units == 'A':
                Columns.update({key: [Columns[key][0], units.au]})
            elif option_units == 'o' or option_units == 'O':
                new_unit = float(int('New unit (variable * new unit): '))
                Columns.update({key: [Columns[key][0], new_unit]})
            else:
                print('ERROR: Invalid option.')

        elif option == 'm':
            print('List of variables: \n')
            for i in enumerate(Data[0]):
                print(str(i[0]-1) + ')',i[1])
            print()
 
            key = input('Select variable to convert (Default=1): ') or '0'
            if int(key) > 0:
                key = str(int(key) + 1) 

            length_units_menu()
            
            option_units = input('Select unit (Default=Msun): ') or 'M'
            if option_units == 'm' or option_units == 'M':
                Columns.update({key: [Columns[key][0], 1]})
            elif option_units == 'g' or option_units == 'G':
                Columns.update({key: [Columns[key][0], units.pdu]})
            elif option_units == 'k' or option_units == 'k':
                Columns.update({key: [Columns[key][0], units.mts]})
            elif option_units == 'm' or option_units == 'M':
                Columns.update({key: [Columns[key][0], units.au]})
            elif option_units == 'o' or option_units == 'O':
                new_unit = float(int('New unit (variable * new unit): '))
                Columns.update({key: [Columns[key][0], new_unit]})
            else:
                print('ERROR: Invalid option.')

        else:
            print()
            print('ERROR: Invalid option.')
    
        print()
        units_main_menu()
        option = input('Enter your option: ')
        





