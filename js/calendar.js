// 月とコマンドライン引数とのMap
// MEMO:Dateオブジェクトは月の値を0~11で表現するため、コマンドライン引数とのマッピングに用いる
const monthMap = new Map([
  ["1", 0],
  ["2", 1],
  ["3", 2],
  ["4", 3],
  ["5", 4],
  ["6", 5],
  ["7", 6],
  ["8", 7],
  ["9", 8],
  ["10", 9],
  ["11", 10],
  ["12", 11],
]);

// 曜日の配列
const dayOfWeek = ["日", "月", "火", "水", "木", "金", "土"];

// メイン処理
try {
  let month;
  const date = new Date();
  const year = date.getFullYear();
  console.log(`date: ${date}`);
  console.log(`year: ${year}`);

  const args = process.argv;
  if (args.length > 2) {
    // コマンドライン引数のチェック処理
    checkCommandLineArgs(args);
    // 指定された月取得
    const monthArg = String(args[3]);
    month = monthMap.get(monthArg);
  } else {
    // 引数を指定しない場合、今月を取得
    month = date.getMonth();
  }

  // 月初日と月末日の取得
  const firstDate = getFirstDate(year, month);
  const lastDate = getLastDate(year, month);
  console.log(`月初日: ${firstDate}`);
  console.log(`月末日: ${lastDate}`);
} catch (err) {
  console.error(err);
  process.exit(1);
}

/**
 * 月初日を取得する
 * @param {number} year 年
 * @param {number} month 月（0~11）
 * @returns 月初日
 */
function getFirstDate(year, month) {
  return new Date(year, month, 1);
}

/**
 * 月末日を取得する
 * @param {number} year 年
 * @param {number} month 月 (0~11)
 * @returns 月末日
 */
function getLastDate(year, month) {
  // 翌月の月初日を取得
  const targetDate =
    month === "11"
      ? new Date(year + 1, month, 1)
      : new Date(year, month + 1, 1);
  // 翌月の月初日から1日引く
  targetDate.setDate(0);
  return targetDate;
}

/**
 * コマンドライン引数をチェックする
 * @param {Array} args コマンドライン引数が格納された配列
 */
function checkCommandLineArgs(args) {
  if (args.length === 4) {
    // -mオプションのチェック
    if (args[2] !== "-m") {
      throw new Error("月を指定する場合は、-mオプションをつけて下さい。");
    }
    // 月の値のチェック（月Mapにない場合はエラー）
    const monthArg = String(args[3]);
    if (!monthMap.has(monthArg)) {
      throw new Error("月の値が不正です。1~12の範囲内で指定して下さい。");
    }
  } else {
    throw new Error(
      "月を指定する場合は、コマンドライン引数を2つ入力して下さい。\n第1引数は -m 第2引数は1~12までの数値です。"
    );
  }
}
