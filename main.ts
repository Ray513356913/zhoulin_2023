function 自动后退 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 0 - 自动巡线速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 0 - 自动巡线速度)
}
function 手动右转 () {
    if (手动电机速度 > 80) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 0.3 * 手动电机速度)
        neZha.setMotorSpeed(neZha.MotorList.M2, -0.3 * 手动电机速度)
    } else {
        neZha.setMotorSpeed(neZha.MotorList.M1, 0.5 * 手动电机速度)
        neZha.setMotorSpeed(neZha.MotorList.M2, -0.5 * 手动电机速度)
    }
}
function 第三段 () {
    右转找黑线()
    自动巡线速度 = 40
    巡线毫秒(1800)
    neZha.stopAllMotor()
    basic.pause(1000)
    if (_123位置 == 1) {
        basic.showNumber(1)
    } else if (_123位置 == 2) {
        basic.showNumber(2)
    } else if (_123位置 == 3) {
        basic.showNumber(3)
    }
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Four, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(300)
    左右轮差速(60, -10)
    basic.pause(700)
    neZha.stopAllMotor()
    basic.pause(200)
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1))) {
        左右轮差速(25, -25)
    }
    neZha.stopAllMotor()
    basic.pause(300)
    自动巡线速度 = 25
    巡线毫秒(150)
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.One, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    左右轮差速(35, 35)
    basic.pause(400)
    neZha.stopAllMotor()
    basic.pause(300)
    左右轮差速(55, -50)
    basic.pause(700)
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1))) {
        左右轮差速(55, -50)
    }
    neZha.stopAllMotor()
    basic.pause(800)
    左右轮差速(-40, -40)
    basic.pause(300)
    neZha.stopAllMotor()
    basic.pause(300)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 180)
    basic.pause(300)
    if (_123位置 == 1) {
        _1号轨道()
    } else if (_123位置 == 2) {
        _2号轨道2()
    } else if (_123位置 == 3) {
        _3号轨道3()
    }
}
function 亮灯32 () {
    if (ABC位置 == 2 || ABC位置 == 4) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Blue))
    } else if (ABC位置 == 1 || ABC位置 == 6) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Yellow))
    } else if (ABC位置 == 3 || ABC位置 == 5) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Red))
    }
}
function 巡线毫秒 (数字: number) {
    初始时间 = input.runningTime()
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(数字 < input.runningTime() - 初始时间)) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
}
function 舵机复位 () {
    // 倒球
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 170)
    // 捡球
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S2, 245)
    // 前叉
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    // 升旗1
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S4, 315)
}
function 手动阶段 () {
    if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.LEFT) || PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Squ)) {
        if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.UP)) {
            左转前进()
        } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.DOWN)) {
            左转后退()
        } else {
            手动左转()
        }
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.RIGHT) || PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Cir)) {
        if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.UP)) {
            右转前进()
        } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.DOWN)) {
            右转后退()
        } else {
            手动右转()
        }
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.UP)) {
        手动前进()
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.DOWN)) {
        手动后退()
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Right1)) {
        if (倒球角度S1 >= 238) {
            倒球角度S1 += 0
        } else {
            倒球角度S1 += 2
        }
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 倒球角度S1)
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Right2)) {
        倒球角度S1 = 170
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S1, 倒球角度S1)
        basic.pause(10)
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Tri)) {
        手动电机速度 = 50
        if (捡球角度S2 >= 185) {
            捡球角度S2 += 0
        } else {
            捡球角度S2 += 10
        }
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S2, 捡球角度S2)
        basic.pause(10)
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.X)) {
        手动电机速度 = 50
        if (捡球角度S2 <= 140) {
            捡球角度S2 += 0
        } else {
            捡球角度S2 += -20
        }
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S2, 捡球角度S2)
        basic.pause(10)
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Sele)) {
        手动电机速度 = 50
        if (捡球角度S2 >= 240) {
            捡球角度S2 += 0
        } else if (捡球角度S2 >= 180) {
            捡球角度S2 += 40
        } else {
            捡球角度S2 += 10
        }
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S2, 捡球角度S2)
        basic.pause(10)
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Left1)) {
        手动电机速度 = 100
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    } else if (PlanetX_Basic.get_Attention_Value(PlanetX_Basic.value_level.Left2)) {
        手动电机速度 = 100
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 150)
    } else {
        neZha.stopAllMotor()
    }
}
function 自动前进 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 自动巡线速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 自动巡线速度)
}
function 亮灯33 () {
    if (ABC位置 == 1 || ABC位置 == 3) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Blue))
    } else if (ABC位置 == 2 || ABC位置 == 5) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Yellow))
    } else if (ABC位置 == 4 || ABC位置 == 6) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Red))
    }
}
function 左转后退 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 0 - 手动电机速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 0 - 0.15 * 手动电机速度)
}
function 右转前进 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 手动电机速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 0.15 * 手动电机速度)
}
function 高级巡线 () {
    PlanetX_Basic.Trackbit_get_state_value()
    if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_11) || PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_3)) {
        自动左转()
    } else if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_14) || PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_2)) {
        自动右转()
    } else if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_12)) {
        while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1))) {
            左右轮差速(80, 0)
        }
    } else if (PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_8)) {
        while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1))) {
            左右轮差速(0, 80)
        }
    } else {
        自动前进()
    }
}
input.onButtonPressed(Button.A, function () {
    if (ABC位置 < 6) {
        ABC位置 += 1
        basic.pause(200)
    } else {
        ABC位置 = 1
        basic.pause(200)
    }
    ABC位置显示图案()
})
function 自动左转 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 5)
    neZha.setMotorSpeed(neZha.MotorList.M2, 1 * 自动巡线速度)
}
function _3号轨道3 () {
    自动巡线速度 = 23
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.One, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(800)
    自动前进()
    basic.pause(300)
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Four, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(800)
    巡线毫秒(600)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 210)
    basic.pause(200)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    basic.pause(200)
    自动巡线速度 = 25
    巡线毫秒(900)
    neZha.stopAllMotor()
}
function 右转后退 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 0 - 0.15 * 手动电机速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 0 - 手动电机速度)
}
function 右转找黑线 () {
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1))) {
        左右轮差速(30, -30)
    }
    neZha.stopAllMotor()
}
function 亮灯31 () {
    if (ABC位置 == 5 || ABC位置 == 6) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Blue))
    } else if (ABC位置 == 3 || ABC位置 == 4) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Yellow))
    } else if (ABC位置 == 1 || ABC位置 == 2) {
        strip.showColor(PlanetX_Display.colors(PlanetX_Display.NeoPixelColors.Red))
    }
}
function ABC位置显示图案 () {
    if (ABC位置 == 1) {
        // ABC
        basic.showLeds(`
            . . # . .
            . . . # .
            . . # . #
            . . . # .
            . . # . .
            `)
    } else if (ABC位置 == 2) {
        // ACB
        basic.showLeds(`
            . . # . .
            . . . # .
            . . # . #
            . # . # .
            . . . . .
            `)
    }
    if (ABC位置 == 3) {
        // BAC
        basic.showLeds(`
            . . # . .
            . # . # .
            . . . . #
            . . . # .
            . . # . .
            `)
    } else if (ABC位置 == 4) {
        // BCA
        basic.showLeds(`
            . . # . .
            . # . # .
            . . # . #
            . # . . .
            . . . . .
            `)
    }
    if (ABC位置 == 5) {
        // CAB
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            . . . # .
            . . . . .
            `)
    } else if (ABC位置 == 6) {
        // CBA
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            . . . . .
            . . . . .
            `)
    }
}
function 第二段 () {
    basic.clearScreen()
    自动巡线速度 = 40
    左转找黑线()
    basic.pause(300)
    巡线毫秒(2100)
    neZha.stopAllMotor()
    basic.pause(300)
    自动巡线速度 = 25
    strip.clear()
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Four, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(500)
    自动巡线速度 = 30
    巡线毫秒(950)
    neZha.stopAllMotor()
    basic.pause(500)
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Four, PlanetX_Basic.TrackbitType.State_1))) {
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(0, -40)
    }
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1))) {
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(0, -40)
    }
    neZha.stopAllMotor()
    basic.pause(300)
    巡线毫秒(200)
    // 前叉
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 170)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S4, 180)
    basic.pause(300)
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_5))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(300)
    左右轮差速(35, 35)
    basic.pause(700)
    neZha.stopAllMotor()
    basic.pause(500)
    左右轮差速(-25, -25)
    basic.pause(100)
    neZha.stopAllMotor()
    for (let index = 0; index < 3; index++) {
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 235)
        basic.pause(200)
        左右轮差速(-25, -25)
        basic.pause(100)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 215)
        basic.pause(200)
    }
    左右轮差速(-25, -25)
    basic.pause(200)
    neZha.stopAllMotor()
    basic.pause(500)
    for (let index = 0; index < 3; index++) {
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 235)
        basic.pause(200)
        左右轮差速(-25, -25)
        basic.pause(100)
        neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 215)
        basic.pause(200)
    }
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 140)
    左右轮差速(-25, -25)
    basic.pause(500)
    neZha.stopAllMotor()
    basic.pause(500)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    basic.pause(200)
}
function 手动后退 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 0 - 手动电机速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 0 - 手动电机速度)
}
function 左转前进 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 0.15 * 手动电机速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 手动电机速度)
}
function 左转找黑线 () {
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1))) {
        左右轮差速(-30, 30)
    }
    neZha.stopAllMotor()
}
function _2号轨道2 () {
    自动巡线速度 = 23
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.One, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(800)
    巡线毫秒(700)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 210)
    basic.pause(200)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    basic.pause(200)
    自动巡线速度 = 25
    巡线毫秒(1600)
    neZha.stopAllMotor()
}
function 左右轮差速 (M1: number, M2: number) {
    neZha.setMotorSpeed(neZha.MotorList.M1, M1)
    neZha.setMotorSpeed(neZha.MotorList.M2, M2)
}
function _1号轨道 () {
    自动巡线速度 = 23
    for (let index = 0; index < 2; index++) {
        巡线毫秒(730)
        neZha.stopAllMotor()
        basic.pause(500)
    }
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 210)
    basic.pause(200)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    basic.pause(200)
    自动巡线速度 = 25
    巡线毫秒(2500)
    neZha.stopAllMotor()
}
input.onButtonPressed(Button.B, function () {
    PlanetX_AILens.initModule()
    PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.Card)
    if (_123位置 < 3) {
        _123位置 += 1
        basic.pause(200)
    } else {
        _123位置 = 1
        basic.pause(200)
    }
    basic.showNumber(_123位置)
})
function 手动前进 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 手动电机速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 手动电机速度)
}
function 第四段 () {
    自动巡线速度 = 25
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S4, 315)
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1) && (PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Three, PlanetX_Basic.TrackbitType.State_1) && PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Four, PlanetX_Basic.TrackbitType.State_1)))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    neZha.stopAllMotor()
    basic.pause(800)
    自动巡线速度 = 30
    巡线毫秒(840)
    neZha.stopAllMotor()
    basic.pause(800)
    左右轮差速(30, -30)
    basic.pause(350)
    neZha.stopAllMotor()
    basic.pause(800)
    while (!(PlanetX_Basic.TrackbitChannelState(PlanetX_Basic.TrackbitChannel.Two, PlanetX_Basic.TrackbitType.State_1))) {
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(0, -40)
    }
    neZha.stopAllMotor()
    basic.pause(800)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 150)
    basic.pause(200)
    自动巡线速度 = 25
    巡线毫秒(500)
    neZha.stopAllMotor()
    basic.pause(800)
    左右轮差速(25, 25)
    basic.pause(600)
    neZha.stopAllMotor()
    basic.pause(300)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S4, 30)
    basic.pause(1500)
    左右轮差速(-40, -40)
    basic.pause(500)
    neZha.stopAllMotor()
    basic.pause(200)
    neZha.setServoAngel(neZha.ServoTypeList._360, neZha.ServoList.S3, 240)
    左右轮差速(-30, 30)
    basic.pause(300)
    左转找黑线()
    自动巡线速度 = 40
    巡线毫秒(200)
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_0))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    左右轮差速(40, 100)
    basic.pause(800)
    neZha.stopAllMotor()
}
function 第一段 () {
    自动巡线速度 = 25
    basic.pause(100)
    左右轮差速(80, 80)
    basic.pause(700)
    neZha.stopAllMotor()
    basic.pause(200)
    左右轮差速(-40, 40)
    basic.pause(170)
    巡线毫秒(300)
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_5))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    巡线毫秒(200)
    自动巡线速度 = 35
    neZha.stopAllMotor()
    basic.pause(200)
    左右轮差速(40, -40)
    basic.pause(500)
    neZha.stopAllMotor()
    // 亮灯3-3
    亮灯33()
    basic.pause(3000)
    左右轮差速(-40, 40)
    basic.pause(500)
    neZha.stopAllMotor()
    // 亮灯3-2
    亮灯32()
    basic.pause(2000)
    PlanetX_Basic.Trackbit_get_state_value()
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_5))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    巡线毫秒(200)
    neZha.stopAllMotor()
    basic.pause(200)
    左右轮差速(-35, 35)
    basic.pause(200)
    neZha.stopAllMotor()
    basic.pause(500)
    // 亮灯3-1
    亮灯31()
    basic.pause(500)
    左右轮差速(35, -35)
    basic.pause(200)
    neZha.stopAllMotor()
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_5))) {
        PlanetX_Basic.Trackbit_get_state_value()
        高级巡线()
    }
    巡线毫秒(400)
    左右轮差速(35, -35)
    basic.pause(150)
    neZha.stopAllMotor()
    basic.pause(200)
    左右轮差速(50, 50)
    basic.pause(100)
    while (!(PlanetX_Basic.TrackbitState(PlanetX_Basic.TrackbitStateType.Tracking_State_5))) {
        PlanetX_Basic.Trackbit_get_state_value()
        左右轮差速(50, 50)
    }
    basic.pause(150)
    neZha.stopAllMotor()
    basic.pause(300)
}
function 自动右转 () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 1 * 自动巡线速度)
    neZha.setMotorSpeed(neZha.MotorList.M2, 5)
}
function 手动左转 () {
    if (手动电机速度 > 80) {
        neZha.setMotorSpeed(neZha.MotorList.M1, -0.3 * 手动电机速度)
        neZha.setMotorSpeed(neZha.MotorList.M2, 0.3 * 手动电机速度)
    } else {
        neZha.setMotorSpeed(neZha.MotorList.M1, -0.5 * 手动电机速度)
        neZha.setMotorSpeed(neZha.MotorList.M2, 0.5 * 手动电机速度)
    }
}
let 初始时间 = 0
let 自动巡线速度 = 0
let 手动电机速度 = 0
let 捡球角度S2 = 0
let 倒球角度S1 = 0
let strip: PlanetX_Display.Strip = null
let ABC位置 = 0
let _123位置 = 0
basic.clearScreen()
_123位置 = 0
ABC位置 = 0
舵机复位()
neZha.stopAllMotor()
strip = PlanetX_Display.create(PlanetX_Display.DigitalRJPin.J1, 24, PlanetX_Display.NeoPixelMode.RGB)
倒球角度S1 = 170
捡球角度S2 = 245
手动电机速度 = 100
自动巡线速度 = 40
basic.showNumber(0)
// 230518
basic.forever(function () {
    if (PlanetX_Basic.Crash(PlanetX_Basic.DigitalRJPin.J2)) {
        舵机复位()
        第一段()
        第二段()
        第三段()
        第四段()
    } else {
        手动阶段()
    }
})
