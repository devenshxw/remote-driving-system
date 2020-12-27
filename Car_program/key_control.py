#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO


# 小车电机引脚定义
# A表示车辆左侧，B表示右侧
AIN1 = 21
AIN2 = 20
BIN1 = 26
BIN2 = 19
ENA = 16
ENB = 13


PWM_MAX = 2000

pwma_speed = 85
pwmb_speed = 85

# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)


# 忽略警告信息
GPIO.setwarnings(False)


def ss_start():
    """启动"""
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)
    # 设置pwm引脚和频率为2000hz
    pwm_ENA = GPIO.PWM(ENA, PWM_MAX)
    pwm_ENB = GPIO.PWM(ENB, PWM_MAX)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


def ss_stop():
    """停止"""
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()


def tm_p():
    """P挡"""
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(0)


def tm_r():
    """R挡"""
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)


def tm_n():
    """N挡"""
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(0)


def tm_d():
    """D挡"""
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)


def turn_left():
    """左转"""
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)


def turn_right():
    """右转"""
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)


def speed_down():
    """减速"""
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)

    
def speed_up():
    """加速"""
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)
    time.sleep(0.1)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(0)


def work(signal):
    """信号解析"""
    # 停止
    if signal == "000000":
        ss_stop()
    # 启动
    elif signal == "100000":
        ss_start()
    # P挡
    elif signal == "010000":
        tm_p()
    # R挡
    elif signal == "020000":
        tm_r()
    # N挡
    elif signal == "030000":
        tm_n()
    # D挡
    elif signal == "040000":
        tm_d()
    # 左转
    elif signal == "001000":
        turn_left()
    # 右转
    elif signal == "000100":
        turn_right()
    # 减速
    elif signal == "000010":
        speed_down()
    # 加速
    elif signal == "000001":
        speed_up()
    else:
        pass


if __name__ == '__main__':
    work(signal)