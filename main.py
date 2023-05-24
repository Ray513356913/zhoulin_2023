def 自动后退():
    neZha.set_motor_speed(neZha.MotorList.M1, 0 - 自动巡线速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 0 - 自动巡线速度)
def 手动右转():
    if 手动电机速度 > 80:
        neZha.set_motor_speed(neZha.MotorList.M1, 0.3 * 手动电机速度)
        neZha.set_motor_speed(neZha.MotorList.M2, -0.3 * 手动电机速度)
    else:
        neZha.set_motor_speed(neZha.MotorList.M1, 0.5 * 手动电机速度)
        neZha.set_motor_speed(neZha.MotorList.M2, -0.5 * 手动电机速度)
def 第三段():
    global 自动巡线速度
    右转找黑线()
    自动巡线速度 = 40
    巡线毫秒(1900)
    neZha.stop_all_motor()
    basic.pause(1000)
    if _123位置 == 1:
        basic.show_number(1)
    elif _123位置 == 2:
        basic.show_number(2)
    elif _123位置 == 3:
        basic.show_number(3)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1) and (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1))):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(300)
    左右轮差速(60, -10)
    basic.pause(1200)
    neZha.stop_all_motor()
    basic.pause(200)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        左右轮差速(25, -25)
    neZha.stop_all_motor()
    basic.pause(300)
    自动巡线速度 = 30
    巡线毫秒(150)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1) and (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.ONE,
        PlanetX_Basic.TrackbitType.STATE_1))):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    左右轮差速(35, 35)
    basic.pause(400)
    neZha.stop_all_motor()
    basic.pause(300)
    左右轮差速(55, -50)
    basic.pause(700)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1)):
        左右轮差速(55, -50)
    neZha.stop_all_motor()
    basic.pause(800)
    左右轮差速(-40, -40)
    basic.pause(200)
    neZha.stop_all_motor()
    basic.pause(300)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 180)
    basic.pause(300)
    if _123位置 == 1:
        _1号轨道()
    elif _123位置 == 2:
        _2号轨道2()
    elif _123位置 == 3:
        _3号轨道3()
    neZha.stop_all_motor()
    basic.pause(300)
def 亮灯32():
    if ABC位置 == 2 or ABC位置 == 4:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.BLUE))
    elif ABC位置 == 1 or ABC位置 == 6:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.YELLOW))
    elif ABC位置 == 3 or ABC位置 == 5:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.RED))
def 巡线毫秒(数字: number):
    global 初始时间
    初始时间 = input.running_time()
    PlanetX_Basic.Trackbit_get_state_value()
    while not (数字 < input.running_time() - 初始时间):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
def 舵机复位():
    # 倒球
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 170)
    # 捡球
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S2, 245)
    # 前叉
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    # 升旗1
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S4, 335)
def 手动阶段():
    global 倒球角度S1, 手动电机速度, 捡球角度S2
    if PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.LEFT) or PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.SQU):
        if PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.UP):
            左转前进()
        elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.DOWN):
            左转后退()
        else:
            手动左转()
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.RIGHT) or PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.CIR):
        if PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.UP):
            右转前进()
        elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.DOWN):
            右转后退()
        else:
            手动右转()
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.UP):
        手动前进()
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.DOWN):
        手动后退()
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.RIGHT1):
        if 倒球角度S1 >= 238:
            倒球角度S1 += 0
        else:
            倒球角度S1 += 2
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 倒球角度S1)
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.RIGHT2):
        倒球角度S1 = 170
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S1, 倒球角度S1)
        basic.pause(10)
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.TRI):
        手动电机速度 = 50
        if 捡球角度S2 >= 185:
            捡球角度S2 += 0
        else:
            捡球角度S2 += 10
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S2, 捡球角度S2)
        basic.pause(10)
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.X):
        手动电机速度 = 50
        if 捡球角度S2 <= 140:
            捡球角度S2 += 0
        else:
            捡球角度S2 += -20
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S2, 捡球角度S2)
        basic.pause(10)
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.SELE):
        手动电机速度 = 50
        if 捡球角度S2 >= 240:
            捡球角度S2 += 0
        elif 捡球角度S2 >= 180:
            捡球角度S2 += 40
        else:
            捡球角度S2 += 10
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S2, 捡球角度S2)
        basic.pause(10)
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.LEFT1):
        手动电机速度 = 100
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    elif PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.LEFT2):
        手动电机速度 = 100
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 150)
    else:
        neZha.stop_all_motor()
def 自动前进():
    neZha.set_motor_speed(neZha.MotorList.M1, 自动巡线速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 自动巡线速度)
def 亮灯33():
    if ABC位置 == 1 or ABC位置 == 3:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.BLUE))
    elif ABC位置 == 2 or ABC位置 == 5:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.YELLOW))
    elif ABC位置 == 4 or ABC位置 == 6:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.RED))
def 左转后退():
    neZha.set_motor_speed(neZha.MotorList.M1, 0 - 手动电机速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 0 - 0.15 * 手动电机速度)
def 右转前进():
    neZha.set_motor_speed(neZha.MotorList.M1, 手动电机速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 0.15 * 手动电机速度)
def 高级巡线():
    PlanetX_Basic.Trackbit_get_state_value()
    if PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_11) or PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_3):
        自动左转()
    elif PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_14) or PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_2):
        自动右转()
    elif PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_12):
        while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
            PlanetX_Basic.TrackbitType.STATE_1)):
            左右轮差速(80, 0)
    elif PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_8):
        while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
            PlanetX_Basic.TrackbitType.STATE_1)):
            左右轮差速(0, 80)
    else:
        自动前进()

def on_button_pressed_a():
    global ABC位置
    if ABC位置 < 6:
        ABC位置 += 1
        basic.pause(200)
    else:
        ABC位置 = 1
        basic.pause(200)
    ABC位置显示图案()
input.on_button_pressed(Button.A, on_button_pressed_a)

def 自动左转():
    neZha.set_motor_speed(neZha.MotorList.M1, 5)
    neZha.set_motor_speed(neZha.MotorList.M2, 1 * 自动巡线速度)
def _3号轨道3():
    global 自动巡线速度
    自动巡线速度 = 25
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.ONE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(800)
    自动前进()
    basic.pause(300)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(1200)
    巡线毫秒(620)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 210)
    basic.pause(200)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 245)
    basic.pause(200)
    自动巡线速度 = 25
    巡线毫秒(600)
    neZha.stop_all_motor()
def 右转后退():
    neZha.set_motor_speed(neZha.MotorList.M1, 0 - 0.15 * 手动电机速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 0 - 手动电机速度)
def 右转找黑线():
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        左右轮差速(30, -30)
    neZha.stop_all_motor()
def 亮灯31():
    if ABC位置 == 5 or ABC位置 == 6:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.BLUE))
    elif ABC位置 == 3 or ABC位置 == 4:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.YELLOW))
    elif ABC位置 == 1 or ABC位置 == 2:
        strip.show_color(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.RED))
def ABC位置显示图案():
    if ABC位置 == 1:
        # ABC
        basic.show_leds("""
            . . # . .
                        . . . # .
                        . . # . #
                        . . . # .
                        . . # . .
        """)
    elif ABC位置 == 2:
        # ACB
        basic.show_leds("""
            . . # . .
                        . . . # .
                        . . # . #
                        . # . # .
                        . . . . .
        """)
    if ABC位置 == 3:
        # BAC
        basic.show_leds("""
            . . # . .
                        . # . # .
                        . . . . #
                        . . . # .
                        . . # . .
        """)
    elif ABC位置 == 4:
        # BCA
        basic.show_leds("""
            . . # . .
                        . # . # .
                        . . # . #
                        . # . . .
                        . . . . .
        """)
    if ABC位置 == 5:
        # CAB
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . . . #
                        . . . # .
                        . . . . .
        """)
    elif ABC位置 == 6:
        # CBA
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . # . #
                        . . . . .
                        . . . . .
        """)
def 第二段():
    global 自动巡线速度
    basic.clear_screen()
    自动巡线速度 = 40
    左转找黑线()
    basic.pause(300)
    巡线毫秒(2400)
    neZha.stop_all_motor()
    basic.pause(300)
    自动巡线速度 = 30
    strip.clear()
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(500)
    自动巡线速度 = 30
    巡线毫秒(990)
    neZha.stop_all_motor()
    basic.pause(500)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(0, -40)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(0, -40)
    neZha.stop_all_motor()
    basic.pause(300)
    巡线毫秒(200)
    # 前叉
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 170)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S4, 180)
    basic.pause(300)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_5)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(300)
    左右轮差速(35, 35)
    basic.pause(700)
    neZha.stop_all_motor()
    basic.pause(500)
    左右轮差速(-25, -25)
    basic.pause(200)
    neZha.stop_all_motor()
    for index in range(3):
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 235)
        basic.pause(200)
        左右轮差速(-25, -25)
        basic.pause(100)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 215)
        basic.pause(200)
    左右轮差速(-25, -25)
    basic.pause(200)
    neZha.stop_all_motor()
    basic.pause(500)
    for index2 in range(3):
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 235)
        basic.pause(200)
        左右轮差速(-25, -25)
        basic.pause(100)
        neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 215)
        basic.pause(200)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 140)
    左右轮差速(-25, -25)
    basic.pause(500)
    neZha.stop_all_motor()
    basic.pause(500)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    basic.pause(200)
    左右轮差速(25, 25)
    basic.pause(400)
    neZha.stop_all_motor()
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S4, 90)
def 手动后退():
    neZha.set_motor_speed(neZha.MotorList.M1, 0 - 手动电机速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 0 - 手动电机速度)
def 左转前进():
    neZha.set_motor_speed(neZha.MotorList.M1, 0.15 * 手动电机速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 手动电机速度)
def 左转找黑线():
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1)):
        左右轮差速(-30, 30)
    neZha.stop_all_motor()
def _2号轨道2():
    global 自动巡线速度
    自动巡线速度 = 25
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.ONE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(800)
    巡线毫秒(600)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 210)
    basic.pause(200)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 245)
    basic.pause(200)
    自动巡线速度 = 25
    巡线毫秒(1200)
    neZha.stop_all_motor()
def 左右轮差速(M1: number, M2: number):
    neZha.set_motor_speed(neZha.MotorList.M1, M1)
    neZha.set_motor_speed(neZha.MotorList.M2, M2)
def _1号轨道():
    global 自动巡线速度
    自动巡线速度 = 25
    for index3 in range(2):
        巡线毫秒(420)
        neZha.stop_all_motor()
        basic.pause(800)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 210)
    basic.pause(200)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 245)
    basic.pause(200)
    自动巡线速度 = 25
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.ONE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    巡线毫秒(1000)
    neZha.stop_all_motor()

def on_button_pressed_b():
    global _123位置
    if _123位置 < 3:
        _123位置 += 1
        basic.pause(200)
    else:
        _123位置 = 1
        basic.pause(200)
    basic.show_number(_123位置)
input.on_button_pressed(Button.B, on_button_pressed_b)

def 手动前进():
    neZha.set_motor_speed(neZha.MotorList.M1, 手动电机速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 手动电机速度)
def 第四段():
    global 自动巡线速度
    自动巡线速度 = 25
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S4, 335)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1) and (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1) and PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1))):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    neZha.stop_all_motor()
    basic.pause(800)
    自动巡线速度 = 30
    巡线毫秒(660)
    neZha.stop_all_motor()
    basic.pause(800)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.FOUR,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(30, -30)
    neZha.stop_all_motor()
    basic.pause(800)
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.TWO,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(30, -30)
    neZha.stop_all_motor()
    basic.pause(800)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 150)
    basic.pause(200)
    左右轮差速(25, 25)
    basic.pause(600)
    neZha.stop_all_motor()
    basic.pause(300)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S4, 0)
    basic.pause(1500)
    左右轮差速(-40, -40)
    basic.pause(500)
    neZha.stop_all_motor()
    basic.pause(200)
    neZha.set_servo_angel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    左右轮差速(-30, 30)
    basic.pause(300)
    左转找黑线()
    自动巡线速度 = 40
    巡线毫秒(200)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_0)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    左右轮差速(40, 100)
    basic.pause(800)
    neZha.stop_all_motor()
def 第一段():
    global 自动巡线速度
    自动巡线速度 = 25
    basic.pause(100)
    左右轮差速(80, 80)
    basic.pause(700)
    neZha.stop_all_motor()
    basic.pause(200)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_channel_state(PlanetX_Basic.TrackbitChannel.THREE,
        PlanetX_Basic.TrackbitType.STATE_1)):
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(-25, 25)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_5)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    巡线毫秒(200)
    自动巡线速度 = 35
    neZha.stop_all_motor()
    basic.pause(200)
    左右轮差速(40, -40)
    basic.pause(500)
    neZha.stop_all_motor()
    # 亮灯3-3
    亮灯33()
    basic.pause(3000)
    左右轮差速(-40, 40)
    basic.pause(500)
    neZha.stop_all_motor()
    # 亮灯3-2
    亮灯32()
    basic.pause(2000)
    PlanetX_Basic.Trackbit_get_state_value()
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_5)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    巡线毫秒(200)
    neZha.stop_all_motor()
    basic.pause(200)
    左右轮差速(-35, 35)
    basic.pause(200)
    neZha.stop_all_motor()
    basic.pause(500)
    # 亮灯3-1
    亮灯31()
    basic.pause(500)
    左右轮差速(35, -35)
    basic.pause(200)
    neZha.stop_all_motor()
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_5)):
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    巡线毫秒(400)
    左右轮差速(35, -35)
    basic.pause(150)
    neZha.stop_all_motor()
    basic.pause(200)
    左右轮差速(50, 50)
    basic.pause(100)
    while not (PlanetX_Basic.trackbit_state(PlanetX_Basic.TrackbitStateType.TRACKING_STATE_5)):
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(50, 50)
    basic.pause(150)
    neZha.stop_all_motor()
    basic.pause(300)
def 自动右转():
    neZha.set_motor_speed(neZha.MotorList.M1, 1 * 自动巡线速度)
    neZha.set_motor_speed(neZha.MotorList.M2, 5)
def 手动左转():
    if 手动电机速度 > 80:
        neZha.set_motor_speed(neZha.MotorList.M1, -0.3 * 手动电机速度)
        neZha.set_motor_speed(neZha.MotorList.M2, 0.3 * 手动电机速度)
    else:
        neZha.set_motor_speed(neZha.MotorList.M1, -0.5 * 手动电机速度)
        neZha.set_motor_speed(neZha.MotorList.M2, 0.5 * 手动电机速度)
初始时间 = 0
自动巡线速度 = 0
手动电机速度 = 0
捡球角度S2 = 0
倒球角度S1 = 0
strip: PlanetX_Display.Strip = None
ABC位置 = 0
_123位置 = 0
basic.clear_screen()
_123位置 = 0
ABC位置 = 0
舵机复位()
neZha.stop_all_motor()
strip = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J1,
    24,
    PlanetX_Display.NeoPixelMode.RGB)
倒球角度S1 = 170
捡球角度S2 = 245
手动电机速度 = 100
自动巡线速度 = 40
basic.show_number(0)
# 230524

def on_forever():
    if PlanetX_Basic.crash(PlanetX_Basic.DigitalRJPin.J2):
        PlanetX_AILens.init_module()
        PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.CARD)
        basic.clear_screen()
        舵机复位()
        第一段()
        第二段()
        第三段()
        第四段()
    else:
        手动阶段()
basic.forever(on_forever)
