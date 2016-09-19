sum = 1

3.step(1001,2) do | i |
  sum += 4*(i*i) - 6* (i-1)
end

puts sum