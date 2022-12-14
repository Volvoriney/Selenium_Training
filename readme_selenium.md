### WebDriver - Methods and Props
    
    Find Methods
    
    find_element_by_id(self, id_)
    find_elements_by_id(self, id_)
    find_element_by_xpath(self, xpath)
    find_elements_by_xpath(self, xpath)
    find_element_by_link_text(self, link_text)
    find_elements_by_link_text(self, text)
    find_element_by_partial_link_text(self, link_text)
    find_elements_by_partial_link_text(self, link_text)
    find_element_by_name(self, name)
    find_elements_by_name(self, name)
    find_element_by_tag_name(self, name)
    find_elements_by_tag_name(self, name)
    find_element_by_class_name(self, name)
    find_elements_by_class_name(self, name)
    find_element_by_css_selector(self, css_selector)
    find_elements_by_css_selector(self, css_selector)
    
    
    Properties
    
    title
    current_url
    page_source
    current_window_handle
    window_handles
    switch_to
    desired_capabilities
    file_detector
    orientation
    application_cache
    log_types
    
    
    Methods
    
    def get(self, url):
    def execute_script(self, script, *args):
    def execute_async_script(self, script, *args):
    close(self)
    quit(self)
    maximize_window(self)
    fullscreen_window(self)
    minimize_window(self)
    switch_to_active_element(self)
    switch_to_window(self, window_name)
    switch_to_frame(self, frame_reference)
    switch_to_default_content(self)
    switch_to_alert(self)
    back(self)
    forward(self)
    refresh(self)
    get_cookies(self)
    get_cookie(self, name)
    delete_cookie(self, name)
    delete_all_cookies(self)
    add_cookie(self, cookie_dict)
    implicitly_wait(self, time_to_wait)
    set_script_timeout(self, time_to_wait)
    set_page_load_timeout(self, time_to_wait)
    find_element(self, by=By.ID, value=None)
    find_elements(self, by=By.ID, value=None)
    get_screenshot_as_file(self, filename)
    save_screenshot(self, filename)
    get_screenshot_as_png(self)
    get_screenshot_as_base64(self)
    set_window_size(self, width, height, windowHandle='current')
    get_window_size(self, windowHandle='current')
    set_window_position(self, x, y, windowHandle='current')
    get_window_position(self, windowHandle='current')
    get_window_rect(self)
    set_window_rect(self, x=None, y=None, width=None, height=None)
    file_detector(self, detector)
    orientation(self, value)
    get_log(self, log_type)
    
    
    WebDriver - Expected conditions
    
    expected condition
    
    title_is(object)
    title_contains(object)
    presence_of_element_located(object)
    url_contains(object)
    url_matches(object)
    url_to_be(object)
    url_changes(object)
    visibility_of_element_located(object)
    visibility_of(object)
    presence_of_all_elements_located(object)
    visibility_of_any_elements_located(object)
    visibility_of_all_elements_located(object)
    text_to_be_present_in_element(object)
    text_to_be_present_in_element_value(object)
    frame_to_be_available_and_switch_to_it(object)
    invisibility_of_element_located(object)
    invisibility_of_element(invisibility_of_element_located)
    element_to_be_clickable(object)
    staleness_of(object)
    element_to_be_selected(object)
    element_located_to_be_selected(object)
    element_selection_state_to_be(object)
    element_located_selection_state_to_be(object)
    number_of_windows_to_be(object)
    new_window_is_opened(object)
    alert_is_present(object)


### WebElement

    WebElement - Methods and Props

    Properties
    
    tag_name
    text
    location_once_scrolled_into_view
    size
    location
    rect
    screenshot_as_png
    parent
    id
    
    
    Methods
    
    click(self)
    submit(self)
    clear(self)
    get_property(self, name)
    get_attribute(self, name)
    is_selected(self)
    is_enabled(self)
    send_keys(self, *value)
    is_displayed(self)
    value_of_css_property(self, property_name)
    screenshot_as_base64(self)
    screenshot(self, filename)
    find_element(self, by=By.ID, value=None)
    find_elements(self, by=By.ID, value=None)