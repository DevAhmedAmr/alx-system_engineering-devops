#!/usr/bin/env ruby
matches = ARGV[0].scan(/from:(\+?\d{11})|to:(\+?\d{11})|flags:([0-9:-]+)/).flatten
output = matches.reject { |match| match.nil? }.join(",")
puts output
