var add = function(v){
  let result = function(p) {return add(p + v)}
  result.val = v
  return result;
}
Function.prototype.valueOf = function(){return this.val;}