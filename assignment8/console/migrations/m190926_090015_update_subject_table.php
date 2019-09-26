<?php

use yii\db\Migration;

/**
 * Class m190926_090015_update_subject_table
 */
class m190926_090015_update_subject_table extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->dropColumn('subject', 'create_at', $this->integer());
        $this->dropColumn('subject', 'create_by', $this->integer());
        $this->dropColumn('subject', 'update_at', $this->integer());
        $this->dropColumn('subject', 'update_by', $this->integer());
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m190926_090015_update_subject_table cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m190926_090015_update_subject_table cannot be reverted.\n";

        return false;
    }
    */
}
