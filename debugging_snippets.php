<?php


########################################################################################
// Whatsapp debug
$is_direct = '1';
$constant = $is_direct ? FINTOODIRECT_CONS : FINTOOINVEST_CONS;
$wsmessage_content = "";
wscurl($wsmessage_content,$is_direct);
die;
########################################################################################

########################################################################################
// Curl call
$is_direct = '0';
$constant = $is_direct ? FINTOODIRECT_CONS : FINTOOINVEST_CONS;

$url = '';
$postdata = '';
$method = '';

$curldata['url'] = $url;
$curldata['is_direct'] = ($is_direct) ? 1 : 0;
$curldata['postdata'] = $postdata;
$curldata['method'] = $method;
curlcall($curldata);
die;
########################################################################################

#################################################################################################################
// Mysqli connection
$port = "3306";
$host = "localhost";
$dbname = "localfh";
$user = "root";
$pass = "root@123";
$db = new mysqli($host, $user, $pass, $dbname);
if ($db->connect_errno) { echo "Failed to connect to MySQL: " . $db->connect_error; exit(); }
$q1 = "";
$res = $db->query($q1);
if (!$res) echo ("Error description: " . $db->error);
while ($row = $res->fetch_assoc()) { r_print($row);}
$db->close();

#################################################################################################################

#################################################################################################################
// Pick invest migration code

$port = "3306";
$host = "localhost";
$dbname = "localfh";
$user = "root";
$pass = "root@123";
$localdb = new mysqli($host, $user, $pass, $dbname);
if ($localdb->connect_errno){ echo "Failed to connect to MySQL: " . $db->connect_error; exit(); }

$q1 = "Select id, plans_img_url,plans_img_alttext from pick_invest_plans";
$res = $localdb->query($q1);
$localdb->close();
$res = $localdb->fetch_all(MYSQLI_ASSOC);
$localdb->close();

/* Stage db conn
$host = "13.234.114.226";
$dbname = "fhmain";
$user = "root";
$pass = "SdD@$!(%UR&%^12";
$stagedb = new mysqli($host, $user, $pass, $dbname);
if ($stagedb->connect_errno){ echo "Failed to connect to MySQL: " . $stagedb->connect_error; exit(); } 
echo("Error description: " . $mysqli -> error);
$stagedb->close();
$res = $res2->fetch_all(MYSQLI_ASSOC);*/

/* Live db conn
$host = '52.66.15.35';
$dbname = 'fhmain';
$user = 'inmotionuser';
$pass = '@WS@n/W!-!ere**anY';
$livedb = new mysqli($host, $user, $pass, $dbname);
if ($livedb->connect_errno){ echo "Failed to connect to MySQL: " . $livedb->connect_error; exit(); } 
echo("Error description: " . $livedb -> error);

$altq = "SELECT country_id, country_name FROM countries";
$res2 = $stagedb->query($altq);
$stagedb->close();
$res = $res2->fetch_all(MYSQLI_ASSOC);*/

$altq = "ALTER TABLE `pick_invest_plans`   
	ADD COLUMN `plans_img_alttext` VARCHAR(255) NULL AFTER `plans_img_url`";
$res2 = $stagedb->query($altq);

foreach($data as $row){
    $q = "Update pick_invest_plans set plans_img_alttext = '".$row['plans_img_alttext']."' where id='".$row['id']."' and plans_img_url='".$row['plans_img_url']."'";
    $res1 = $stagedb->query($q);
    if(!$res1) echo "<br>failed";
    // $res1->free(); 
}
echo "done";
$stagedb->close();

#################################################################################################################

########################################################################################
// Whatsapp aof debug
//transaction_ws.php fpsetaofstatus,sefaofstatus
$is_direct = '0';
$status = "1";
$constant = $is_direct ? FINTOODIRECT_CONS : FINTOOINVEST_CONS;
$uname = "Abhishek";
$wsmessage_content = "Dear test,\nYour Investment Account is active now and is ready for Investments. Take the first step towards better tomorrow. Start Investing now by clicking test\nTeam Fintooinvest.";
wscurl($wsmessage_content, $is_direct);
die;
########################################################################################

########################################################################################
// SMS debug
$is_direct = '0';
$constant = $is_direct ? FINTOODIRECT_CONS : FINTOOINVEST_CONS;
$sms_dlt_id = '1307163966105768448';
$msg = "Gentle reminder for your next Premium-Future Generali India Life Insurance Co. Ltd on May 01, 2022. for Rs. 217360. For any urgent query, call us on +91-9699 800600. Team Fintooinvest";
smscurl($msg, $sms_dlt_id, $is_direct);
die;
########################################################################################


########################################################################################
// maturity health ins debugging code


$is_direct = '1';
$constant = $is_direct ? FINTOODIRECT_CONS : FINTOOINVEST_CONS;
$user_name = "Abhishek";
$amount = 90000;

$data['issuer'] = $data['insurance_company_name'] = "TEST Company";
// $sms_dlt_id = $is_direct == 1 ? HEALTHINSMATRENEW_DIRECT_SMS_DLTID : HEALTHINSMATRENEW_SMS_DLTID;
// $sms_dlt_id = $is_direct == 1 ? FDBONDMAT_DIRECT_SMS_DLTID : FDBONDMAT_SMS_DLTID;


// $message_content = "Dear " . $user_name . ",\nYour Health Insurance Policy from " . $data['insurance_company_name'] . " is due for renewal on " . "09/03/1997" . ".\nRequest you to renew it before the due date to avoid any lapses.\nYour premium amount is " . $amount . "\nFor any help or query, call us at " . online_support . ".\nRegards,\nTeam " . $constant;

// $message_content = "Dear " . $user_name . ",\nYour FD/BOND - " . $data['issuer'] . " worth " . $amount . " is getting matured on " . "09/03/1997" . ".\nCall us on " . online_support . " to know more.\nRegards,\nTeam " . $constant;

// smscurl($message_content, $sms_dlt_id, $is_direct);

$wsmessage_content = "Dear " . $user_name . ",\nYour Health Insurance Policy from " . $data['insurance_company_name'] . " is due for renewal on " . "09/03/1997" . ".\nRequest you to renew it before the due date to avoid any lapses.\nYour premium amount is " . $amount . "\nFor any help or query, call us at " . "9702163787" . ".\nRegards,\nTeam " . $constant;

// $wsmessage_content = "Dear " . $user_name . ",\nYour FD/BOND - " . $data['issuer'] . " worth " . $amount . " is getting matured on " . "09/03/1997" . ".\nRequest you to call us on " . online_support . " to know more or initiate the further process.\nRegards,\nTeam " . $constant;


// $wsmessage_content = "Dear TEST,\nYour FD/BOND - COMPANY worth Rs.1000000 is getting matured on 09-03-1997.\nRequest you to call us on 9702163787 to know more or initiate the further process.\nRegards,\nTeam Fintooinvest";

$wsmessage_content = "Dear Abhishek,\nYour FD/BOND - Fintoo worth Rs.10000 is getting matured on 09-03-1997.\nRequest you to call us on 9702163787 to know more or initiate the further process.\nRegards,\nTeam Fintoo";

// FD/BOND Maturity


// $header = "Health Insurance Renewal";
$header = "FD/BOND Maturity";
// $header = "";

wscurl($wsmessage_content, $is_direct, $header);
die;

/* Dear {{1}},
Your Health Insurance Policy from {{2}} is due for renewal on {{3}}.
Request you to renew it before the due date to avoid any lapses.
Your premium amount is {{4}}
For any help or query, call us at {{5}}.
Regards,
Team Fintooinvest */

########################################################################################

########################################################################################
// PHP excel read data
require('/var/www/FH-Stage/fintooinvest/PHPExcel/classes/PHPExcel.php');
require('/var/www/FH-Stage/fintooinvest/PHPExcel/classes/PHPExcel/IOFactory.php');
$target_file = "/home/puja/Downloads/temp/schemecodewithprimary.csv";
$excelReader = PHPExcel_IOFactory::createReaderForFile($target_file);
$excelReader->setReadDataOnly(true);
$excelObj = $excelReader->load($target_file);
$var = $excelObj->getActiveSheet()->toArray(null, true, true, true);
$highestColumm = $excelObj->setActiveSheetIndex(0)->getHighestColumn(); // e.g. "EL" 
$highestRow = $excelObj->setActiveSheetIndex(0)->getHighestRow();

$highestColumm++;
$sc_old = array();
for ($row = 1; $row < $highestRow + 1; $row++) {
    $dataset = array();
    for ($column = 'A'; $column != $highestColumm; $column++) {
        $dataset[] = str_replace("'", "", $excelObj->setActiveSheetIndex(0)->getCell($column . $row)->getValue());
        //  if ($column == 'G' && $row != 1) {
        // array_push($sc_old, str_replace("'", "", $excelObj->setActiveSheetIndex(0)->getCell($column . $row)->getValue()));
        // } 
        if (empty($sc_old[$dataset[0]])) {
            $sc_old[$dataset[0]] = $dataset[32];
        }
    }
}

// Utilities::rPrint($sc_old);
$res = array();
foreach ($sc_old as $key => $val) {
    $temp = array();
    if (!empty($sc_new[$key])) {
        if ($sc_old[$key] != $sc_new[$key]) {
            $temp['sc_key'] = $key;
            $temp['sc_old_val'] = $sc_old[$key];
            $temp['sc_new_val'] = $sc_new[$key];
        }
    }
    if (!empty($temp)) {
        $res[] = $temp;
    }
}

Utilities::rPrint($res);
########################################################################################

########################################################################################
// Compare excel files
$target_file = "/home/puja/Downloads/temp/Annexure-IDFC.xls";
$excelReader = PHPExcel_IOFactory::createReaderForFile($target_file);
$excelReader->setReadDataOnly(true);
$excelObj = $excelReader->load($target_file);
$var = $excelObj->getActiveSheet()->toArray(null, true, true, true);
$highestColumm = $excelObj->setActiveSheetIndex(0)->getHighestColumn(); // e.g. "EL" 
$highestRow = $excelObj->setActiveSheetIndex(0)->getHighestRow();

$highestColumm++;
$annex_countries = array();
for ($row = 1; $row < $highestRow + 1; $row++) {
    $dataset = array();
    for ($column = 'A'; $column != $highestColumm; $column++) {
        $dataset[] = str_replace("'", "", $excelObj->setActiveSheetIndex(0)->getCell($column . $row)->getValue());
    }
    $annex_countries[] = $dataset[1];
}

$annex_countries = array_flip($annex_countries);
// Utilities::rPrint($annex_countries);
/* 
$target_file = "/home/puja/Downloads/temp/countries_db.csv";
$excelReader = PHPExcel_IOFactory::createReaderForFile($target_file);
$excelReader->setReadDataOnly(true);
$excelObj = $excelReader->load($target_file);
$var = $excelObj->getActiveSheet()->toArray(null, true, true, true);
$highestColumm = $excelObj->setActiveSheetIndex(0)->getHighestColumn(); // e.g. "EL" 
$highestRow = $excelObj->setActiveSheetIndex(0)->getHighestRow();

$highestColumm++;
$countries = array();
for ($row = 1; $row < $highestRow + 1; $row++) {
    $dataset = array();
    for ($column = 'A'; $column != $highestColumm; $column++) {
        $dataset[] = str_replace("'", "", $excelObj->setActiveSheetIndex(0)->getCell($column . $row)->getValue());
        //  if ($column == 'G' && $row != 1) {
        // array_push($countries, str_replace("'", "", $excelObj->setActiveSheetIndex(0)->getCell($column . $row)->getValue()));
        // }
    }
    $countries[] = $dataset[0];
}

$countries = array_flip($countries);
// Utilities::rPrint($countries); */


$host = '52.66.15.35';
$dbname = 'fhmain';
$user = 'inmotionuser';
$pass = '@WS@n/W!-!ere**anY';

$stagedb = new mysqli($host, $user, $pass, $dbname);
if ($stagedb->connect_errno) {
    echo "Failed to connect to MySQL: " . $stagedb->connect_error;
    exit();
}

$altq = "SELECT country_id, country_name FROM countries";
$res2 = $stagedb->query($altq);
$stagedb->close();
$res = $res2->fetch_all(MYSQLI_ASSOC);

foreach ($res as $key => $val) {
    $countries[$val['country_name']] = $val['country_id'];
}

// exit;

$res = array();
$tempmatched = array();
$tempunmatched = array();
foreach ($annex_countries as $key => $val) {
    if (isset($countries[$key])) {
        $tempmatched[$key] = $countries[$key];
    } else {
        $tempunmatched[] = $key;
    }
}

// $matching_countrycode = implode(",", array_values($tempmatched));
$matching_cname = implode("','", $tempunmatched);
echo $matching_countrycode;

$res = array(
    'matched' => $tempmatched,
    'unmatched' => $tempunmatched
);

Utilities::rPrint($res);

########################################################################################

########################################################################################
// dash-trans-details.php
// Debugging Snippets for wbrs inv val round off

unlink('/var/www/html/test.log');
// if ($pan == 'AUFPV0822N') {
$isinstocheck = array('INF247L01AH0', 'INF247L01700', 'INF247L01AT5');
$isinstocheckMirae = array('INF769K01HH0', 'INF769K01HG2', 'INF769K01HF4', 'INF769K01HS7', 'INF769K01HU3', 'INF769K01HT5', 'INF769K01HP3', 'INF769K01HR9', 'INF769K01HQ1');
$showMotilalO = $showMirae = false;
$count = 0;
foreach ($wbrs as $key => $val) {
    $count++;
    if (empty($val['isin'])) {
        continue;
    }

    if (in_array($val['isin'], $isinstocheck)) {
        $showMotilalO = true;
        $addpur_key = array_search('Additional Purchase', $val['valid_for']);
        $stopsip_key = array_search('Stop SIP', $val['valid_for']);
        unset($wbrs[$key]['valid_for'][$addpur_key]);
        unset($wbrs[$key]['valid_for'][$stopsip_key]);
    }

    if (in_array($val['isin'], $isinstocheckMirae)) {
        $showMirae = true;
        $addpur_key = array_search('Additional Purchase', $val['valid_for']);
        $switch_key = array_search('Switch', $val['valid_for']);
        $stopstp_key = array_search('Start STP', $val['valid_for']);
        unset($wbrs[$key]['valid_for'][$addpur_key]);
        unset($wbrs[$key]['valid_for'][$switch_key]);
        unset($wbrs[$key]['valid_for'][$stopstp_key]);
    }
    // Utilities::fintooLog('/abhishek/test.log', ' Scheme Name: ' . print_r($val['scheme_name'], 1));
    /* $temparr = [];
    $temparr['scheme_name'] = $val['scheme_name'];
    $temparr['invested_cost'] = $val['invested_cost'];
    $temparr['curr_value'] = $val['curr_value'];
    $temparr['units'] = $val['units'];
    $total_inv = 0;
    $total_units = 0;
    foreach ($val['transactin_detail'] as $inner_trxns) {
      if ($inner_trxns['inv_amount'] < 0) {
        continue;
      }
      $temp_inner = [];
      $temp_inner['transaction_date'] = $inner_trxns['transaction_date'];
      $temp_inner['inv_amount'] = $inner_trxns['inv_amount'];
      $temp_inner['purchase_price'] = $inner_trxns['purchase_price'];
      $temp_inner['units'] = $inner_trxns['units'];
      $temp_inner['total_val'] = $inner_trxns['units'] * $inner_trxns['purchase_price'];
      $temp_inner['curr_nav'] = $inner_trxns['curr_nav'];
      // $temp_inner['curr_value'] = $inner_trxns['curr_value'];
      $temp_inner['comm_units'] = $inner_trxns['comm_units'];
      $total_inv +=  $inner_trxns['inv_amount'];
      $total_units +=  $inner_trxns['units'];
      $temp_inner['total_inv'] = $total_inv;
      $temp_inner['total_units'] = $total_units;

      $temparr['transactin_detail'][] = $temp_inner;
    } */
    // Utilities::fintooLog('/abhishek/test.log', ' $temparr: ' . print_r($temparr, 1));
}
// }

########################################################################################
