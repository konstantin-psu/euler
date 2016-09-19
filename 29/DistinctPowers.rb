require 'set'

s = Set.new []
max = 100

2.step(max,1) do | i |
  2.step(max,1) do | j |
    s << i ** j
  end
end

puts s.size

