function add(a, b) {
  let maxLength = Math.max(a.length, b.length);
    a = a.padStart(maxLength, "0");
    b = b.padStart(maxLength, "0");
    let result = "";
    let carry = 0;
    for (let i = maxLength - 1; i >= 0; i--) {
        let currSum = parseInt(a[i]) + parseInt(b[i]) + carry;
        if (currSum >= 10) {
            carry = 1;
            currSum = currSum % 10;
        } else {
            carry = 0;
        }
        result = currSum + result;
    }
    if (carry > 0) {
        result = carry + result;
    }
    return result;
}
