can you explain the max_atrp_SO_distance? is that a % like the max_pump_atrp? We use the 
max_pump_atrp as reference for a good max_atrp_SO_distance                                 

The `max_atrp_SO_distance` is a user-defined input in the script that represents the maximum distance, as a multiple of the Average True Range Percentage (ATRP), for the last safety order (SO) from the initial order price. It is not a percentage like `max_pump_atrp`, but rather a multiplier that determines how far the last SO should be placed relative to the volatility of the market, as measured by ATRP.

For example, if `max_atrp_SO_distance` is set to 3.0, it means that the distance for the last SO will be 3 times the daily ATRP value away from the initial order price. This distance is used to calculate the placement of each SO, with the spacing between SOs increasing non-linearly from the first to the last SO.

The `max_pump_atrp` is a calculated value that represents the maximum percentage price increase from the initial short order price, normalized by the daily ATRP. It is used as a reference to understand the maximum volatility experienced by an asset in terms of its ATRP.

If you want to use `max_pump_atrp` as a reference for setting a good `max_atrp_SO_distance`, you could consider setting `max_atrp_SO_distance` to a value based on the historical `max_pump_atrp` observed. For instance, if historically `max_pump_atrp` has been around 2.5, you might set `max_atrp_SO_distance` to a slightly higher value to ensure that your SOs cover a range of volatility that has been seen in the past.

If you need any changes to the code based on this explanation, please let me know what specific changes you would like to make.

The `max_pump_atrp` and `max_drop_atrp` values are indeed percentages that represent the maximum price increase or decrease relative to the initial price, normalized by the daily ATRP. When you see a value like 3.03 in the table for `max_pump_atrp`, it means that the maximum price pump was 303% of the daily ATRP.

On the other hand, `max_atrp_SO_distance` is a multiplier used to determine the distance for safety order placements based on the daily ATRP. It is not a percentage but a factor that scales the ATRP value.

If you observe a `max_pump_atrp` of 3.03 (or 303% of the daily ATRP) and you want to set the `max_atrp_SO_distance` based on this observation, you can indeed choose a value like 3.5 as a conservative estimate to cover a range of volatility that has been seen in the past. This would mean that your last safety order would be placed at a distance of 350% of the daily ATRP from the initial order price.

You do not need to convert one to the other since they are both relative to the ATRP, but you are using them for different purposes. `max_pump_atrp` is a historical observation of volatility, while `max_atrp_SO_distance` is a parameter for setting the distance of safety orders.

If you want to adjust the `max_atrp_SO_distance` input in the script based on the historical `max_pump_atrp`, you would simply enter the new value directly as the input. No code change is necessary unless you want to automate this process or add some logic related to this adjustment. If you need such a feature, please provide more details on how you would like it to work.

### this is where it went wrong...

'+our strategy takes an entry order and if price goes against, we take another order (SO order) so that average price stays closer to price. Our TP moves as well allowing us to exit easier.  These SOs are triggered based on % price adverse move against (threshold) when preice reaches threshold the 1st SO is execucted, additional SOs are executed in similar way but the distance may be adjusted by user input safe_order_step_scale.  review the code and we can work on next task related to the SO placement. 'price_deviation = input.float(0.06, title='Price deviation to open safety orders (%)','

'+we are imagining allowing user to choose an alternative method for the SO placement based on ATRP, similar to the max_drop_atrp and max_pump_atrp, user can enter max_atrp_SO_distance and this would set the last SO placement from the initial_order. then we can take the max_safe_order and calculate thier distances from initial_order to the max_atrp_SO_distance, ideally we also have control on how they are spaced.  Typically they are close together at beginning and spread out until max. IE distance from SO1 to SO2 small, but if max SO6 then distance from SO5 to SO6 much larger'