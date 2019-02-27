/**
 * 将字符串中的空格替换成 %20
 * @param {String} str
 */
function replaceSpace(str) {
  if(!str || typeof str !== 'string') {
    if(str.length === 0) {
      return str
    }

    console.log('参数必须是字符串')
    return
  }

  let strArr = str.split('')
  let len = strArr.length,
      spaceCount = 0 // 空格数目

  for(let i = 0; i < len; i++) {
    if(strArr[i] === ' ') {
      spaceCount++
    }
  }

  let newLen = len + 2 * spaceCount // 替换后字符串的长度
  
  for(let i = len, j = newLen; i >= 0 && i !== j; i--) {
    if(strArr[i] !== ' ') { // 如果不是空格字符，则复制
      strArr[j--] = strArr[i]
    }else {
      strArr[j--] = '0'
      strArr[j--] = '2'
      strArr[j--] = '%'
    }
  }

  return strArr.join('')
}

// let str = 'hello world'
// let result = replaceSpace(str)
// console.log(result)

console.log(replaceSpace(''))
console.log(replaceSpace(' '))
console.log(replaceSpace('hello'))
console.log(replaceSpace('he   llo'))

// console.log(str.replace(' ', '%20'))
