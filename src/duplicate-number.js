/**
 * 找出数组中任意一个重复的数字
 * 数组长度 n, 数组中元素的值为 0~n-1
 */

/**
 * 解法一：
 * 将数组进行排序，在排序后的数组中找重复元素
 * 循环遍历数组，如果后一个元素与前一个元素相等，则说明找到了重复的元素
 * 否则继续往后查找
 * @param {Array} arr 
 */
function findDupNum(arr) {
  let find = false,
    result

  if (!arr || !(arr instanceof Array)) {
    throw new Error('arr must be an Array')
  } else {
    let sorted = arr.sort(sortArray) // 对数组进行排序

    for (let i = 1, len = sorted.length; i < len; i++) {
      if (sorted[i] === sorted[i - 1]) { // 如果前后两个数字相同，则说明找到重复元素
        result = sorted[i]
        find = true
        return result
      }
    }

    if (!find) {
      console.log('数组中不存在重复的元素')
    }
  }
}

// 数组排序
function sortArray(num1, num2) {
  return num1 - num2
}

/**
 * 解法二：
 * 用一个结果数组存放对应值，结果数组中索引值与值对应
 * 如果当前索引已存在与其相等的值，则说明存在重复元素
 * @param {Array} arr
 */
function findDupNum1(arr) {
  if (!arr || !(arr instanceof Array)) {
    throw new Error('arr must be an Array')
  }

  let findArr = [] // 用来存放处理后的数组
  let find = false

  for(let i = 0, len = arr.length; i < len; i++) {
    let currentNum = arr[i]

    if(findArr[currentNum] !== currentNum) { // 如果结果数组中 currentNum 对应位置没有值，则将 currentNum 放入对应位置
      findArr[currentNum] = currentNum
    }else { // 如果结果数组中 currentNum 对应位置有值为 currentNum，则说明找到重复元素
      find = true
      return currentNum
    }
  }

  if(!find) {
    console.log('数组中不存在重复的元素')
  }
}

/**
 * 解法三：
 * 对数组进行排序，把元素放在与其值相等的索引位置
 * 如果对应位置已经存在相等的值，则说明找到重复元素
 * @param {Array} arr
 */
function findDupNum2(arr) {
  if (!arr || !(arr instanceof Array)) {
    throw new Error('arr must be an Array')
  }

  let find = false,
      temp // 用于存放临时值

  for(let i = 0, len = arr.length; i < len; i++) {
    let currentNum = arr[i]

    if(currentNum !== i) {
      temp = arr[currentNum]

      if(temp === currentNum) {
        find = true
        return currentNum
      }else {
        arr[currentNum] = currentNum
        arr[i] = temp
      }
    }
  }

  if(!find) {
    console.log('数组中不存在重复的元素')
  }
}

let a = [2, 3, 1, 0, 2, 3, 5]
let num = findDupNum2([0,1,2,1])
console.log(num)
