#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import RPi.GPIO as GPIO
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


# 小车电机引脚定义
# A表示车辆左侧，B表示右侧
AIN1 = 21
AIN2 = 20
BIN1 = 26
BIN2 = 19
ENA = 16
ENB = 13


PWM_MAX = 2000
IDLE_SPEED = 0.01 * PWM_MAX

# 设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)


# 忽略警告信息
GPIO.setwarnings(False)


# 电机引脚初始化操作
def motor_init():
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


# 小车前进
def run(pwma_speed, pwmb_speed):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)


# 小车后退
def back(pwma_speed, pwmb_speed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)


# 小车左转
def left(pwma_speed, pwmb_speed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)


# 小车右转
def right(pwma_speed, pwmb_speed):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)


# 小车停止
def brake(pwma_speed, pwmb_speed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.pwma_speed = IDLE_SPEED
        self.pwmb_speed = IDLE_SPEED

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_S:
            print("按下S ==> 启动/停止")
            time.sleep(2)
            motor_init()

        elif e.key() == Qt.Key_P:
            print("按下P ==> P档")
        elif e.key() == Qt.Key_R:
            print("按下R ==> R挡")
        elif e.key() == Qt.Key_N:
            print("按下N ==> N挡")
        elif e.key() == Qt.Key_D:
            print("按下D ==> D挡")
            run(self.pwma_speed, self.pwmb_speed)

        elif e.key() == Qt.Key_J:
            print("按下J ==> 前进1步")
            self.pwma_speed += 1
            self.pwmb_speed += 1
            run(self.pwma_speed, self.pwmb_speed)
        elif e.key() == Qt.Key_K:
            print("按下K ==> 后退1步")
        elif e.key() == Qt.Key_H:
            print("按下H ==> 左转1步")
        elif e.key() == Qt.Key_L:
            print("按下L ==> 右转1步")
        else:
            print("按下其他键")


def main():
    try:
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    main()

pwma_speed = IDLE_SPEED
pwmb_speed = IDLE_SPEED


def ss_stop():
    """停止"""
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()


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
    pwma_speed -= 1
    pwmb_speed -= 1
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)

    
def speed_up():
    """加速"""
    pwma_speed += 1
    pwmb_speed += 1
    pwm_ENA.ChangeDutyCycle(pwma_speed)
    pwm_ENB.ChangeDutyCycle(pwmb_speed)


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


