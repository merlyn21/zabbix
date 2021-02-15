#!/usr/bin/python
# coding: utf-8

import telebot
import sys

import config #файл с настройками


message_chat_id = 'id channel'

bot = telebot.TeleBot(config.token)
bot.send_message(message_chat_id, sys.argv[1])
