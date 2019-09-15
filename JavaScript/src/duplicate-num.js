/**
 * 找出数组中任意一个重复的数字
 * 数组长度 n+1, 数组中元素的值为 1~n
 */

/**
 * 解法一：
 * 借用辅助数组
 * 参考 duplicate-number.js 解法二
 */

/**
 * 解法二：
 * 将 1~n 个数字从中间一分为二
 * 判断前一段中数字出现的次数，如果次数大于前一段数字个数，则说明前一段有重复的；同理，后一段也可以这么判断
 * 递归处理前一段/后一段，知道找到重复数字
 */
function findDupNum(arr) {
  if (!arr || !(arr instanceof Array)) {
    throw new Error('arr must be an Array')
  }

  let arrLen = arr.length

  for(let i = 0; i < arrLen; i++) {
    if(arr[i] < 1 || arr[i] >= arrLen) {
      console.log('数组元素必须在 1~n 之间')
      return
    }
  }

  let start = 1,
      end = arrLen - 1

  while(end >= start) {
    let middleNum = Math.floor((end - start) / 2) + start // 求取中间值 
    let count = findNum(start, middleNum, arr)

    if(end === start) {
      if(count > 1) {
        return start
      }else {
        break
      }
    }

    if(count > (middleNum - start + 1)) {
      end = middleNum
    }else {
        start = middleNum + 1
      }
  }

    if(end < start) {
      console.log('不存在重复元素')
      return
    }
}

function findNum(num1, num2, arr) {
  let count = 0

    for(let j = 0, len = arr.length; j < len; j++) {
      if(arr[j] >= num1 && arr[j] <= num2) {
        count++
      }
    }

  return count
}

let a = [2, 3, 5, 4, 3, 2, 6, 7]
let num = findDupNum(a)
console.log(num)
