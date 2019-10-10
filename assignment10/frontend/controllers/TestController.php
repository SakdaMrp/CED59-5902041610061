<?php

namespace frontend\controllers;

use yii\web\Controller;

class TestController extends \yii\web\Controller 
{
    public function actionIndex() {
        //echo 'data test';
        $data = 'data test';
        return $this->render('index',[
            'xdata'=> $data
        ]);
    }

    public function actionTest() {
        echo 'test2';
        return $this->render('test');
    }
}   